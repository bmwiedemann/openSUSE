#
# spec file for package trace-cmd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           trace-cmd
Version:        2.8.3
Release:        0
Summary:        Configuration tool for Ftrace
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Debuggers
URL:            https://elinux.org/Ftrace
Source0:        trace-cmd-%{version}.tar.bz2
Source1:        trace-cmd-rpmlintrc
Patch1:         makefile-lib64.patch
Patch2:         makefile-bash.patch
Patch3:         0001-trace-cmd-fix-multiple-definition-compiler-errors.patch
BuildRequires:  asciidoc
BuildRequires:  audit-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  swig
%if 0%{?suse_version} > 1200
BuildRequires:  xsltproc
%else
BuildRequires:  libxslt
%endif

%description
trace-cmd is a command-line tool for configuring Ftrace.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags} prefix=%{_prefix} trace-cmd
make %{?_smp_mflags} MANPAGE_DOCBOOK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl doc

%install
%make_install prefix=%{_prefix} install_cmd
%make_install prefix=%{_prefix} install_doc
rm %{buildroot}/%{_mandir}/man1/kernelshark.1
rm -rf %{buildroot}/%{_datadir}/kernelshark

%files
%{_bindir}/trace-cmd
%{_libdir}/trace-cmd
%{_mandir}/man1/trace-cmd*
%{_mandir}/man5/trace-cmd.dat*
%{_datadir}/bash-completion/completions/trace-cmd.bash
%license COPYING

%changelog
