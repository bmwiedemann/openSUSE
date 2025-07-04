#
# spec file for package python-pyinotify
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-pyinotify
Version:        0.9.6
Release:        0
Summary:        Python module for watching filesystems changes
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/seb-m/pyinotify
Source:         https://files.pythonhosted.org/packages/source/p/pyinotify/pyinotify-%{version}.tar.gz
Source1:        pyinotify
# PATCH-FIX_UPSTREAM https://github.com/seb-m/pyinotify/pull/205
Patch0:         make_asyncore_support_optional.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
pyinotify is a Python module for watching filesystems changes. By its design
pyinotify can be used for any kind of fs monitoring.

pyinotify relies on a recent Linux Kernel feature (merged in kernel 2.6.13)
called inotify. inotify is an event-driven notifier, its notifications are
exported from kernel space to user space. The raw interface of inotify is
compounded of three system calls. pyinotify binds these system calls and
provides an implementation on top of them offering a generic and abstract way
to use inotify with Python. Pyinotify doesn't requires much detailed knowledge
of inotify. Moreover, it only needs few statements for initializing, watching,
handling (eventually trough a new separate thread), and processing events
notifications through subclassing. The only things to know is the path of items
to watch, the kind of events to monitor and the actions to execute on these
notifications.

%prep
%autosetup -p1 -n pyinotify-%{version}
# remove unwanted shebang
sed -i '/^#!/ d' python2/pyinotify.py
sed -i "s|#!%{_bindir}/env python|#!%__python2|" python2/examples/*py
sed -i "s|#!%{_bindir}/env python|#!%__python3|" python3/examples/*py

%build
%pyproject_wheel

%install
%pyproject_install
install -D -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/pyinotify
%python_clone -a %{buildroot}%{_bindir}/pyinotify

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pyinotify

%post
%python_install_alternative pyinotify

%postun
%python_uninstall_alternative pyinotify

%files %{python_files}
%license COPYING
%doc ACKS README.md
%doc old/ChangeLog old/NEWS
%doc python3/examples
%python_alternative %{_bindir}/pyinotify
%{python_sitelib}/pyinotify.py
%pycache_only %{python_sitelib}/__pycache__/pyinotify.*.pyc
%{python_sitelib}/pyinotify-%{version}.dist-info

%changelog
