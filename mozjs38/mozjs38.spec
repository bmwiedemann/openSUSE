#
# spec file for package mozjs38
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#               2014 Wolfgang Rosenauer
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global		pre_release .rc0
%global		major 38

Name:           mozjs38
Summary:        JavaScript interpreter
License:        MPL-2.0
Group:          Development/Libraries/Other
Version:        %{major}.2.1
Release:        8%{?dist}
Url:            http://www.mozilla.org/js/
Source0:        https://people.mozilla.org/~sstangl/mozjs-%{version}%{pre_release}.tar.bz2
Source1:        baselibs.conf
Patch1:         mozjs38_missing_zlib_moz_build.patch
Patch2:         mozjs38_missing_python_before_milestone_call.patch
Patch3:         mozjs38_avoid_strncat_warning_inline.patch
Patch4:         mozjs-support-48bit-va.patch
Patch5:         mozilla-sed43.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf213
BuildRequires:  gcc-c++
BuildRequires:  mozilla-nspr-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python
BuildRequires:  python-pip
BuildRequires:  readline-devel
BuildRequires:  zip

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package -n libmozjs-%{major}
Summary:        JavaScript library
Group:          System/Libraries

%description -n libmozjs-%{major}
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/Other
Requires:       libmozjs-%{major} = %{version}-%{release}
Requires:       pkg-config

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n mozjs-%{major}.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Remove zlib directory (to be sure using system version)
rm -rf modules/zlib

%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
cd js/src
autoconf-2.13
%configure --disable-static --with-system-nspr --with-system-zlib \
           --enable-threadsafe --enable-readline --enable-xterm-updates
%{__make} %{?_smp_mflags}

%install
cd js/src
%{makeinstall}
# Upstream does not honor --disable-static yet
%{__rm} -rf %{buildroot}%{_libdir}/libjs_static.ajs
# delete js-config since everything should use the pkg-config file
rm -f %{buildroot}%{_bindir}/js-config
# headers are installed with executable permissions
find %{buildroot}%{_includedir}/mozjs-%{major}/ -type f -print | xargs chmod 644
chmod 644 %{buildroot}%{_libdir}/pkgconfig/*
mv %{buildroot}%{_libdir}/pkgconfig/js.pc %{buildroot}%{_libdir}/pkgconfig/mozjs-%{major}.pc

# Install files, not symlinks to build directory
pushd %{buildroot}%{_includedir}
    for link in `find . -type l`; do
	header=`readlink $link`
	rm -f $link
	cp -p $header $link
    done
popd
cp -p js/src/js-config.h %{buildroot}%{_includedir}/mozjs-%{major}

%clean
%{__rm} -rf %{buildroot}

%post -n libmozjs-%{major} -p /sbin/ldconfig

%postun -n libmozjs-%{major} -p /sbin/ldconfig

%files
# TODO /usr/bin/js and not /usr/bin/js38 that differ from previous js24
%defattr(-,root,root,-)
%doc js/src/README.html LICENSE
%{_bindir}/js

%files -n libmozjs-%{major}
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}

%changelog
