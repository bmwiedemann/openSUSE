#
# spec file for package runawk
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           runawk
Version:        1.6.1
Release:        0
Summary:        Wrapper for AWK interpreter
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://sourceforge.net/projects/runawk/
Source0:        https://github.com/cheusov/runawk/archive/%{version}.tar.gz#/runawk-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  mk-configure >= 0.26.0
BuildRequires:  mk-configure-rpm-macros

%description
RunAWK is a small wrapper for AWK interpreter that helps to write
the standalone programs in AWK. It provides modules for AWK
similar to PERL's "use" command and other powerful features.
Dozens of ready to use modules are also provided.

%package examples
Summary:        Examples for RunAWK
Group:          Documentation/Howto
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
This package contains examples for RunAWK.

%prep
%setup -q

%define env \
export NOSUBDIR=a_getopt

%build
%{env}
%{mkcmake} all

%check
%{env}
export TMPDIR=/tmp
%{mkcmake} test

# Remove unneeded files
rm examples/Makefile examples/*.sh examples/*.in

# Fix the shebang lines
sed -i s,"/usr/bin/env ","/usr/bin/", examples/demo*

%install
%{env}
export DESTDIR=%{buildroot}
%{mkcmake} install

%files
%license doc/LICENSE
%doc doc/NEWS doc/TODO README
%{_bindir}/runawk
%{_mandir}/man1/runawk.1%{?ext_man}
%{_mandir}/man3/runawk_modules.3%{?ext_man}
%{_datadir}/%{name}/

%files examples
%attr(0755, root, root) %doc examples

# TODO:
# - consider packaging alt_getopt as a subpackage
# (uses runawk, isn't used by runawk)

%changelog
