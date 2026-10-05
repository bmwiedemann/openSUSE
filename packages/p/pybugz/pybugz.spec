#
# spec file for package pybugz
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
Name:           pybugz
Version:        0.15
Release:        0
Summary:        Python Bugzilla Interface
License:        GPL-2.0-only
URL:            http://www.liquidx.net/pybugz
Source0:        https://github.com/williamh/pybugz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pybugz-version.patch martin@pluskal.org -- the 0.15 tag
# never bumped __version__, which flit takes from as the dynamic version
Patch0:         pybugz-version.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       pybugz = %{version}
Obsoletes:      pybugz < %{version}
%endif
%python_subpackages

%description
PyBugz is a python and command line interface to Bugzilla.

It was conceived as a tool to speed up the workflow for Gentoo Linux
developers and contributors when dealing with bugs using Bugzilla. By
avoiding the clunky web interface, the user quickly search, isolate and
contribute to the project very quickly. Developers alike can easily extract
attachments and close bugs all from the comfort of the command line.

%package -n %{name}-common
Summary:        Common files for %{name}
Supplements:    python2-%{name}
Supplements:    python3-%{name}

%description -n %{name}-common
PyBugz is a python and command line interface to Bugzilla.

It was conceived as a tool to speed up the workflow for Gentoo Linux
developers and contributors when dealing with bugs using Bugzilla. By
avoiding the clunky web interface, the user quickly search, isolate and
contribute to the project very quickly. Developers alike can easily extract
attachments and close bugs all from the comfort of the command line.

This package contains common files for %{name}.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bugz
%python_clone -a %{buildroot}%{_mandir}/man1/bugz.1
# binary and man page both land in libalternatives/bugz/, so they switch
# together through that config's man= key and need no group=
%fdupes %{buildroot}

install -d -m 0755  %{buildroot}%{_sysconfdir}/pybugz.d

%check
# upstream ships no test suite; bugz.cli pulls in every module, and the
# version is what the wheel got its name from.  -P keeps the cwd source
# tree off sys.path, so this imports the installed module.
%{python_expand #
PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -P -c "import bugz.cli; assert bugz.__version__ == '%{version}', bugz.__version__"
}

%pre
%python_libalternatives_reset_alternative bugz

%files %{python_files}
%license LICENSE
%doc README
%python_alternative %{_bindir}/bugz
%python_alternative %{_mandir}/man1/bugz.1%{ext_man}
%{python_sitelib}/bugz
%{python_sitelib}/pybugz-%{version}.dist-info

%files -n %{name}-common
%dir %{_sysconfdir}/pybugz.d
%{_mandir}/man5/pybugz.d.5%{?ext_man}
%dir %{_datadir}/pybugz.d
%{_datadir}/pybugz.d/busybox.conf
%{_datadir}/pybugz.d/default.conf
%{_datadir}/pybugz.d/freebsd.conf
%{_datadir}/pybugz.d/freedesktop.conf
%{_datadir}/pybugz.d/gentoo.conf
%{_datadir}/pybugz.d/gnome.conf
%{_datadir}/pybugz.d/kernel.conf
%{_datadir}/pybugz.d/libav.conf
%{_datadir}/pybugz.d/llvm.conf
%{_datadir}/pybugz.d/mozilla.conf
%{_datadir}/pybugz.d/redhat.conf
%{_datadir}/bash-completion
%{_datadir}/zsh

%changelog
