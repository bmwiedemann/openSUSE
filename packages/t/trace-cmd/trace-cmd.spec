#
# spec file for package trace-cmd
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.1.5
Release:        0
Summary:        Configuration tool for Ftrace
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git
Source0:        trace-cmd-v%{version}.tar.gz
Patch1:         0001-libtracecmd-Add-initial-support-for-meson.patch
Patch2:         0002-trace-cmd-Add-initial-support-for-meson.patch
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  meson
BuildRequires:  source-highlight
BuildRequires:  xmlto
Recommends:     libtraceevent1-plugins

%description
trace-cmd is a command-line tool for configuring Ftrace.

%package python3
Summary:        Python plugin support for trace-cmd
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}-%{release}
Requires:       python3
BuildRequires:  python3-devel
BuildRequires:  swig
Provides:       %{name}-python = %{version}

%description  python3
Python plugin support for trace-cmd

%prep
%autosetup -p1 -n trace-cmd-v%{version}

%build
%meson \
    -Ddocs-build=true \
    -Dhtmldir=%{_docdir}/%{name}
%meson_build

%install
%meson_install

%fdupes %buildroot/%_prefix

%files
%{_bindir}/trace-cmd
%{_mandir}/man1/trace-cmd*
%{_mandir}/man5/trace-cmd.dat*
%{_docdir}/%{name}/*.html
%{_datadir}/bash-completion/completions/trace-cmd.bash
%license COPYING
%doc README

%files python3
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*.so
%{python3_sitearch}/%{name}/ctracecmd.py
%doc Documentation/README.PythonPlugin

%changelog
