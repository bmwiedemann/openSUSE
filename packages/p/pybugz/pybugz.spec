#
# spec file for package pybugz
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pybugz
Version:        0.13
Release:        0
Summary:        Python Bugzilla Interface
License:        GPL-2.0
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.liquidx.net/pybugz
Source0:        https://github.com/williamh/pybugz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
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
Group:          Development/Languages/Python
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
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bugz
%python_clone -a %{buildroot}%{_mandir}/man1/bugz.1
%fdupes %{buildroot}

install -Dpm 0644  contrib/bash-completion \
  %{buildroot}%{_datadir}/bash-completion/completions/bugz
install -Dpm 0644  contrib/zsh-completion  \
  %{buildroot}%{_datadir}/zsh/site-functions/_bugz
install -d -m 0755  %{buildroot}%{_sysconfdir}/pybugz.d

%post
%{python_install_alternative bugz bugz.1}

%postun
%{python_uninstall_alternative bugz bugz.1}

%files %{python_files}
%doc LICENSE README
%python_alternative %{_bindir}/bugz
%python_alternative %{_mandir}/man1/bugz.1%{ext_man}
%{python_sitelib}/*

%files -n %{name}-common
%dir %{_sysconfdir}/pybugz.d
%{_mandir}/man5/pybugz.d.5%{ext_man}
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
