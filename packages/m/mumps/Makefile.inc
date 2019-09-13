#
#  This file is part of MUMPS 4.9.2, built on Thu Nov  5 07:05:08 UTC 2009
#  Adapted by Adam Powell from Make.inc/Makefile.gfortran.seq, based on
#  Roberto C. Sanchez' adaptation from Make.inc/Makefile.G95.seq, based on
#  Adam Powell's adaptation of Make.inc/Makefile.G95.par
#
#Begin orderings

# NOTE that PORD is distributed within MUMPS by default. If you would like to
# use other orderings, you need to obtain the corresponding package and modify
# the variables below accordingly.
# For example, to have Metis available within MUMPS:
#          1/ download Metis and compile it
#          2/ uncomment (suppress # in first column) lines
#             starting with LMETISDIR,  LMETIS
#          3/ add -Dmetis in line ORDERINGSF
#             ORDERINGSF  = -Dpord -Dmetis
#          4/ Compile and install MUMPS
#             make clean; make   (to clean up previous installation)
#
#          Metis/ParMetis and SCOTCH/PT-SCOTCH (ver 5.1 and later) orderings are now available for MUMPS.
#

#SCOTCHDIR  = /usr
#ISCOTCH    = -I$(SCOTCHDIR)/scotch/include 
# You have to choose one among the following two lines depending on
# the type of analysis you want to perform. If you want to perform only
# sequential analysis choose the first (remember to add -Dscotch in the ORDERINGSF
# variable below); for both parallel and sequential analysis choose the second 
# line (remember to add -Dptscotch in the ORDERINGSF variable below)

#LSCOTCH    = -L$(SCOTCHDIR)/lib -lesmumps -lscotch -lscotcherr
#LSCOTCH    = -L$(SCOTCHDIR)/lib -lptesmumps -lptscotch -lptscotcherr


LPORDDIR = $(topdir)/PORD/lib/
IPORD    = -I$(topdir)/PORD/include/
LPORD    = -L$(LPORDDIR) -lpord

#LMETISDIR = /local/metis/
#IMETIS    = # Metis doesn't need include files (Fortran interface avail.)

# You have to choose one among the following two lines depending on
# the type of analysis you want to perform. If you want to perform only
# sequential analysis choose the first (remember to add -Dmetis in the ORDERINGSF
# variable below); for both parallel and sequential analysis choose the second 
# line (remember to add -Dparmetis in the ORDERINGSF variable below)

#LMETIS    = -L$(LMETISDIR) -lmetis
#LMETIS    = -L$(LMETISDIR) -lparmetis -lmetis

# The following variables will be used in the compilation process.
# Please note that -Dptscotch and -Dparmetis imply -Dscotch and -Dmetis respectively.
#ORDERINGSF = -Dscotch -Dmetis -Dpord -Dptscotch -Dparmetis
ORDERINGSC  = $(ORDERINGSF)

LORDERINGS = $(LMETIS) $(LPORD) $(LSCOTCH)
IORDERINGSF = $(ISCOTCH)
IORDERINGSC = $(IMETIS) $(IPORD) $(ISCOTCH)

#End orderings
########################################################################
################################################################################

#PLAT    =
# Library extension, + C and Fortran "-o" option
# may be different under Windows
LIBEXT  = .a
OUTC    = -o 
OUTF    = -o 

RM = /bin/rm -f
#CC = gcc
#FC = gfortran
#FL = gfortran
#      keep a space at the end if options have to be separated from lib name
AR = ar vr 
#RANLIB = ranlib
RANLIB  = echo
# See point 17 in the FAQ to have more details on the compilation of mpich with gfortran
INCPAR  = -I/usr/include
LIBPAR  = $(SCALAP) $(LAPACK) -L/usr/lib -lmpi
INCSEQ = -I$(topdir)/libseq
LIBSEQ  =  $(LAPACK) -L$(topdir)/libseq -lmpiseq$(PLAT)
#LIBBLAS = -L/usr/lib/xmm/ -lf77blas -latlas
#LIBBLAS = -lblas -llapack
LIBOTHERS = -lpthread
#Preprocessor defs for calling Fortran from C (-DAdd_ or -DAdd__ or -DUPPER)
CDEFS   = -DAdd_

#Begin Optimized options
OPTF    = -O -fPIC
OPTL    = -O -pie
OPTC    = -O -fPIC
#End Optimized options
#INCS = $(INCSEQ)
#LIBS = $(LIBSEQ)
LIBSEQNEEDED =
