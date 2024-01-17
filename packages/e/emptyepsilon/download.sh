#!/bin/bash

#version="$1"
version=$(grep Version: emptyepsilon.spec | awk '{print $NF}')

wget https://github.com/daid/SeriousProton/archive/EE-${version}.tar.gz -O SeriousProton-${version}.tar.gz
wget https://github.com/daid/EmptyEpsilon/archive/EE-${version}.tar.gz -O EmptyEpsilon-${version}.tar.gz

tmp=$(mktemp -d)

tar xzvf EmptyEpsilon-${version}.tar.gz -C "$tmp" EmptyEpsilon-EE-${version}/CMakeLists.txt
MESHOPTIMIZER_VERSION=$(grep "MESHOPTIMIZER_VERSION" "${tmp}/EmptyEpsilon-EE-${version}/CMakeLists.txt" | head -1 | cut -d' ' -f2 | cut -d')' -f1)
wget "https://github.com/zeux/meshoptimizer/archive/refs/tags/v${MESHOPTIMIZER_VERSION}.zip" -O meshoptimizer.zip

tar xzvf SeriousProton-${version}.tar.gz -C "$tmp" SeriousProton-EE-${version}/libs/basis_universal/CMakeLists.txt
BASIS_VERSION=$(grep "BASIS_VERSION" "${tmp}/SeriousProton-EE-${version}/libs/basis_universal/CMakeLists.txt" | head -1 | cut -d'"' -f2)
BASIS_URL=$(grep "BASIS_URL" "${tmp}/SeriousProton-EE-${version}/libs/basis_universal/CMakeLists.txt" | head -1 | cut -d'"' -f2)
wget "${BASIS_URL}/archive/refs/tags/${BASIS_VERSION}.zip" -O basis_universal.zip

rm -r "$tmp"
