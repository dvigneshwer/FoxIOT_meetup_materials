#DESCRIPTION : Docker file to create image for ubuntu with OpenCV
#Version : 1.0
#Date : 7th July 2016
#Author: Vigneshwer

FROM ubuntu:14.04

#To change to root user 
RUN echo 'root:root' | chpasswd

RUN apt-get update &&\
	apt-get -y install wget unzip 

RUN echo "Removing any pre-installed ffmpeg and x264" &&\
	apt-get -yqq remove ffmpeg x264 libx264-dev make

RUN sh -c 'echo "deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse" >> /etc/apt/sources.list'

RUN echo "Installing Dependenices" &&\
	apt-get update &&\
	apt-get -yqq install build-essential libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev default-jdk ant libvtk5-qt4-dev

RUN echo "Downloading OpenCV" &&\		
	wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip &&\
	unzip opencv-2.4.9.zip

RUN cd opencv-2.4.9 &&\
	mkdir build &&\
	cd build &&\
	echo "Current Location :-"$(pwd) &&\
	cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON .. &&\
	make &&\
	make install
	
RUN	sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf' &&\
	ldconfig &&\
	sh -c 'echo "PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig" >> /etc/bash.bashrc' &&\
	sh -c 'echo "export PKG_CONFIG_PATH" >> /etc/bash.bashrc' &&\
	echo "OpenCV ready to be used"

#libdc1394 driver location hard link
RUN echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc

ENTRYPOINT /bin/bash
