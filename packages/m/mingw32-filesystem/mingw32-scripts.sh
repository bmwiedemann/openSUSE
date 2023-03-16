#!/bin/sh -

# mingw32-scripts
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
# macros from mingw32-macros.mingw32 cross-compilation.
#
# It supports the environment variable MINGW32_MACROS=<value> to be
# able to override individual rpm macros. With 
# 
#   MINGW32_MACROS='__cmake ~/bin/cmake' mingw32-cmake
# 
# for example, the specified cmake executable is used instead of
# the internal default.

NAME="_`basename $0|tr -- - _`"
DEFINE=${MINGW32_MACROS:+--define="${MINGW32_MACROS}"}
eval "`rpm "${DEFINE}" --eval "%${NAME} $(printf " %q" "${@}")"`"
