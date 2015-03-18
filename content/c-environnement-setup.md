Title: C++ environnement setup
Date: 14:03 Wed 18 Mar 2015
Tags: dev,env,workflow
Category: dev
Author: pdt
Summary: how to setup c++

[TOC]

# Summary
This document details how to setup a modern C++ environnement in Linux (based on the version of EarthServer)

# Upgrade distribution 
    :::bash
	sudo apt-get update
	sudo apt-get upgrade
   
# Install cmake
	:::bash
	sudo apt-get install cmake
	sudo apt-get install automake autoconf
	sudo apt-get install build-essential bzip2 lynx zile zlib1g-dev git unzip

# Install GCC-4.9 From Source
	:::bash
	sudo apt-get install libgmp3-dev libgmp-dev libmpfr-dev libmpc-dev flex bison libc6-dev gcc-multilib

	sudo mkdir /gcc
	sudo chmod 777 /gcc
	svn co svn://gcc.gnu.org/svn/gcc/trunk /gcc

	cd /gcc
	./contrib/download_prerequisites

	mkdir /gcc/objdir
	cd /gcc/objdir

configure gcc build:
-------------------
View configuration flags used to build the distro version of gcc:

	:::bash
	gcc -v
	../configure -v --enable-languages=c,c++,go --prefix=/usr --program-suffix=-4.9 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-time=yes --enable-gnu-unique-object --enable-plugin --with-system-zlib --disable-ppl-version-check --disable-multilib --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu

build and install:
---------------------

	:::bash
	sudo ln -s /usr/include/x86_64-linux-gnu/zconf.h /usr/include
	sudo ln -s /usr/lib/x86_64-linux-gnu /usr/lib64		
	make -j 8
	sudo make install

Update the gcc and g++ symbolic links
------------------------------------------

	:::bash
	sudo rm /usr/bin/g++
	sudo ln -s /usr/bin/g++-4.9 /usr/bin/g++
		
	sudo rm /usr/bin/gcc
	sudo ln -s /usr/bin/gcc-4.9 /usr/bin/gcc

	sudo rm /usr/bin/cpp
	sudo ln -s /usr/bin/cpp-4.9 /usr/bin/cpp

	sudo rm /usr/bin/gcov
	sudo ln -s /usr/bin/gcov-4.9 /usr/bin/gcov
		
	sudo rm /usr/bin/c++
	sudo ln -s /usr/bin/c++-4.9 /usr/bin/c++
	
Test g++ 4.9
--------------------------------------
edit /tmp/generalized-lambda.cpp:

	:::cpp
    #include <iostream>
    #include <algorithm>

	void f(std::size_t);

	int main()
	{
		int x = 4;
		auto y = [&r = x, x = x+1]()->int {
			r += 2;
			return x+2;
		}();  // Updates ::x to 6, and initializes y to 7.

	    std::cout << y << std::endl;

	    int input;
		std::cin >> input;

	    f(input);

	    return 0;
	}

	void f(std::size_t n)
	{
		int a[n];
		for (std::size_t i = 0; i < n; ++i)
		a[i] = 2*i;
		std::sort(a, a+n);

	    for( int i = 0; i < n; i++) {
		   std::cout << a[i] << " ";
	    }
		std::cout << std::endl;
	}

Build and run:

	:::bash
	cd /tmp; g++-4.9 -std=c++1y generalized-lambda.cpp; ./a.out

Verify which libraries we are linking against:

	:::bash
	ldd a.out

Install Clang
======================
download and build clang from source

	:::bash
	sudo mkdir /llvm
	sudo chmod 777 /llvm
	cd /llvm
	svn co http://llvm.org/svn/llvm-project/llvm/trunk llvm

	cd llvm/tools/
	svn co http://llvm.org/svn/llvm-project/cfe/trunk clang
	cd ../..
	cd llvm/tools/clang/tools
	svn co http://llvm.org/svn/llvm-project/clang-tools-extra/trunk extra
	cd ../../../..
	cd llvm/projects
	svn co http://llvm.org/svn/llvm-project/compiler-rt/trunk compiler-rt
	cd ../..
	mkdir build
	cd build
	../llvm/configure --prefix=/usr/local/llvm-3.4 --bindir=/usr/local/llvm-3.4/bin --enable-cxx11 --enable-optimizedCXX=/usr/bin/g++-4.7 CC=/usr/bin/gcc-4.7

	make -j 8

	sudo make install

edit ~/.bashrc to add /usr/local/llvm-3.4/bin to your path and set CC and CXX accordingly:

	:::bash
	PATH=$PATH:/usr/local/llvm-3.4/bin

	export CC=/usr/local/llvm-3.4/bin/clang
	export CXX=/usr/local/llvm-3.4/bin/clang++

Reload .bashrc

	:::bash
	. ~/.bashrc


Test clang
------------------------
edit /tmp/thread.cpp:

    :::cpp
    #include <iostream>
    #include <thread>

	thread_local int i=0;

	void f(int newval){
		i=newval;
	}

	void g(){
		std::cout<<i;
	}

	void threadfunc(int id){
		f(id);
		++i;
		g();
	}

	int main(){
		i=9;
		std::thread t1(threadfunc,1);
		std::thread t2(threadfunc,2);
		std::thread t3(threadfunc,3);

	    t1.join();
		t2.join();
		t3.join();
		std::cout<<i<<std::endl;
	}


build and run:

	:::bash
	cd /tmp
	clang++ -std=c++11 -fsanitize=memory -fno-omit-frame-pointer -O1 -g -fno-optimize-sibling-calls -pthread thread.cpp
	/tmp/a.out


Install Boost
====================================

install additional libs:
------------------------------------

	:::bash
	sudo apt-get install libicu-dev libicu48 zlib1g zlib1g-dev libbz2 libbz2-dev libbz2-1.0 python-dev

	
remove current boost installation:
----------------------------------------
	:::bash
	sudo apt-get --purge remove libboost*
	sudo rm -rf /usr/include/boost
	sudo rm -rf /usr/lib/libboost*


install boost 1.57 from source
------------------------------------

	:::bash
	sudo mkdir /libboost
	sudo chmod 777 /libboost/
	cd /libboost/
	wget 'http://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.gz/download' -O boost_1_57.tar.gz
	tar -xzvf boost_1_57.tar.gz
	cd boost_1_57_0
	./bootstrap.sh --with-toolset=gcc --with-libraries=all  --prefix=/usr
	./b2 --prefix=/usr toolset=gcc cxxflags="-std=c++11" threading=multi segmented-stacks=on link=static
	sudo ./b2 --prefix=/usr toolset=gcc cxxflags="-std=c++11" threading=multi segmented-stacks=on link=static install

test boost:
-----------------------------
edit /tmp/regex.cpp:

	:::cpp
    #include <boost/regex.hpp>
    #include <iostream>
    #include <string>

	int main()
	{
		std::string line;
		boost::regex pat( "^Subject: (Re: |Aw: )*(.*)" );

	    while (std::cin) {
			std::getline(std::cin, line);
			boost::smatch matches;
			if (boost::regex_match(line, matches, pat))
			std::cout << matches[2] << std::endl;
	    }
     }
	 
build and run with gcc:

	:::bash
	cd /tmp
	g++ -std=c++11 regex.cpp  -lboost_regex
	./a.out
	
build and run with clang:

	:::bash
	cd /tmp
	clang++ -std=c++11 regex.cpp  -lboost_regex
	./a.out

