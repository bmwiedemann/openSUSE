#
# spec file for package python-pyinotify
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyinotify
Version:        0.9.6
Release:        0
Summary:        Python module for watching filesystems changes
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/seb-m/pyinotify
Source:         https://files.pythonhosted.org/packages/source/p/pyinotify/pyinotify-%{version}.tar.gz
Source1:        pyinotify
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%setup -q -n pyinotify-%{version}
# remove unwanted shebang
sed -i '/^#!/ d' python2/pyinotify.py
sed -i "s|#!%{_bindir}/env python|#!%__python2|" python2/examples/*py
sed -i "s|#!%{_bindir}/env python|#!%__python3|" python3/examples/*py

%build
%python_build

%install
%python_install
install -D -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/pyinotify
%python_clone -a %{buildroot}%{_bindir}/pyinotify

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
%{python_sitelib}/*

%changelog
