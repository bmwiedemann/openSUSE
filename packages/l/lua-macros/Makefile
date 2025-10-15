all:
	mkdir -p build && cd build/ \
	&& cmake .. \
		'-GUnix Makefiles' \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo '-DCMAKE_C_FLAGS=-O2 -Wall -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=3 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g' \
		'-DCMAKE_EXE_LINKER_FLAGS=-flto=auto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now' \
		'-DCMAKE_MODULE_LINKER_FLAGS=-flto=auto -Wl,--as-needed' \
		'-DCMAKE_SHARED_LINKER_FLAGS=-flto=auto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now' \
		-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
		-DBUILD_SHARED_LIBS:BOOL=ON \
		-DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
		-DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
		-DLUA_INCLUDE_DIR:PATH=$(shell pkgconf --variable=includedir lua) \
	&& make

clean:
	rm -rf build CMakeCache.txt
