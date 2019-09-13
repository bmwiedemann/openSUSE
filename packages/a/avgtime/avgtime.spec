#
# spec file for package avgtime
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Define just "test" as a package in _multibuild file to distinguish test
# instructions here
%if "@BUILD_FLAVOR@" == ""
%define _test 0
%define name_ext %nil
%else
%define _test 1
%define name_ext -test
%endif

# DMD is available only on x86*. Use LDC with dub otherwise.
%ifarch %{ix86} x86_64
%bcond_without dcompiler_dmd
%else
%bcond_with dcompiler_dmd
%endif

%define         short_name avgtime
Name:           %{short_name}%{?name_ext}
Version:        v0.5.0+4.ffdf200
Release:        0
Summary:        Utility similar to "time", but with repetitions and more statistics
License:        BSL-1.0
Group:          Productivity/Scientific/Math
Url:            https://github.com/jmcabo/%{short_name}
Source0:        %{short_name}-%{version}.tar.xz
%if 0%{?_test}
BuildRequires:  %{short_name}
%else
%if %{with dcompiler_dmd}
BuildRequires:  dmd
BuildRequires:  phobos-devel
%else
BuildRequires:  dub
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
%endif
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#ExcludeArch:    i586

%description
avgtime works like the "time" command, except it accepts an "-r"
argument to specify repetitions and shows more detailed statistics.

If repetitions are specified, then statistics are computed and shown, like
median, mean, and standard deviation.

%prep
%if 0%{?_test}
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}
%else
%setup -q
%endif

%build
%if 0%{?_test}
avgtime --help
%else
# By default we would link against the static lib causing undefined values
# https://forum.dlang.org/post/ubqoqivomxxbkfpuuhif@forum.dlang.org
# https://forum.rejectedsoftware.com/groups/rejectedsoftware.dub/thread/920/
# okurz: I did not find a way to pass the "defaultlib" path through dub but
# avgtime is so simple we can simply use dmd directly
%if %{with dcompiler_dmd}
dmd -defaultlib=:libphobos2.so avgtime.d
%else
# dub works fine with LDC
dub build --build=release
%endif
%endif

%install
%if 0%{?_test}
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}
%else

mkdir -p %{buildroot}%{_bindir}/
install -D %{name} %{buildroot}%{_bindir}/

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE_1_0.txt
%{_bindir}/%{name}

%endif

%changelog
