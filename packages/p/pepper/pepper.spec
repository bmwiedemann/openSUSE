#
# spec file for package pepper
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without git
%bcond_without mercurial
%bcond_without subversion
%bcond_without gnuplot
%bcond_without man
Name:           pepper
Version:        0.3.3
Release:        0
Summary:        Retrieve Statistics and Generate Reports from Source Code Repositories
License:        GPL-3.0
Group:          Development/Tools/Version Control
Url:            http://jgehring.github.io/pepper/
Source:         https://github.com/jgehring/pepper/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# 0.3.3 tarball is not bootstrapped
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{?suse_version} > 1110
# pull in 5.1 specifically
BuildRequires:  lua51-devel
BuildConflicts:	pkgconfig(lua) >= 5.2.0
%else # SLE
BuildRequires:  lua-devel >= 5.0.1
%endif
%if %{with git}
BuildRequires:  git
%endif
%if %{with mercurial}
BuildRequires:  mercurial
BuildRequires:  python-devel >= 2.1
%endif
%if %{with subversion}
BuildRequires:  libapr1-devel >= 1.5.0
BuildRequires:  subversion-devel >= 1.5.0
%endif
%if %{with man}
BuildRequires:  asciidoc
BuildRequires:  xmlto
%endif
%if %{with gnuplot}
BuildRequires:  gnuplot
Recommends:     gnuplot
%endif

%description
pepper is a flexible command-line tool for retrieving statistics and generating
reports from source code repositories. It ships with several graphical and
textual reports, and is easily extendable using the Lua scripting language.
pepper includes support for multiple version control systems, including Git and
Subversion.

%prep
%setup -q

%build
# 0.3.3 tarball is not bootstrapped
./autogen.sh
export SUSE_ASNEEDED=0
%configure \
	%{?_with_git} \
	%{?_with_mercurial} \
	%{?_with_subversion} \
	%{?_with_gnuplot} \
	%{?_with_man} \
	--disable-leveldb \
	--enable-tests

make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/pepper
%{_datadir}/pepper
%if %{with man}
%{_mandir}/man1/%{name}.1%{ext_man}
%endif

%changelog
