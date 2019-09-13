#cmake support for cvsps 
# author: Cristian Rodriguez crrodriguez@suse.de

PROJECT(cvsps C)
SET(CVSPS_VERSION_MAJOR 2)
SET(CVSPS_VERSION_MINOR 1)
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -Wall -DVERSION=\\\"${CVSPS_VERSION_MAJOR}.${CVSPS_VERSION_MINOR}\\\"")
FIND_PACKAGE(ZLIB REQUIRED)
INCLUDE_DIRECTORIES(${CMAKE_SOURCE_DIR})
INCLUDE_DIRECTORIES(${ZLIB_INCLUDE_DIR})

SET(CVSPS_SRCS 
	cache.c		cap.c
	cvs_direct.c  cvsps.c
	list_sort.c  stats.c  
	util.c cbtcommon/debug.c cbtcommon/hash.c
	cbtcommon/text_util.c cbtcommon/sio.c cbtcommon/tcpsocket.c
	)

ADD_EXECUTABLE(cvsps ${CVSPS_SRCS})

TARGET_LINK_LIBRARIES(cvsps ${ZLIB_LIBRARY})

INSTALL(PROGRAMS cvsps DESTINATION bin)
INSTALL(FILES cvsps.1 DESTINATION share/man/man1)
