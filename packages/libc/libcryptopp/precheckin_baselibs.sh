#!/bin/bash
rm baselibs.conf
echo "libcryptopp$(ls -1 *tar.gz |cut -b 10)_$(ls -1 *tar.gz |cut -b 12)_$(ls -1 *tar.gz |cut -b 14)" > baselibs.conf
echo "" >> baselibs.conf
