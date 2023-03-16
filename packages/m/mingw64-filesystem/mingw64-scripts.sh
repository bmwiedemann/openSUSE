#!/bin/sh -

# mingw64-scripts
# Copyright (C) 2008 Red Hat Inc., Richard W.M. Jones.
# Copyright (C) 2008 Levente Farkas
# Copyright (C) 2023 Ralf Habacker
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

# This is a useful command-line script through which one can use the
# macros from mingw64-macros.mingw64 cross-compilation.
#
# It supports the environment variable MINGW64_MACROS=<value> to be
# able to override individual rpm macros. With 
# 
#   MINGW64_MACROS='__cmake ~/bin/cmake' mingw64-cmake
# 
# for example, the specified cmake executable is used instead of
# the internal default.

NAME="_`basename $0|tr -- - _`"
DEFINE=${MINGW64_MACROS:+--define="${MINGW64_MACROS}"}
eval "`rpm "${DEFINE}" --eval "%${NAME} $(printf " %q" "${@}")"`"
