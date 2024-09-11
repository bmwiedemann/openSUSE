#
# spec file for package python-django-eremaea2
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-django-eremaea2
Version:        2.0.21
Release:        0
Summary:        A simple Django application to store and show webcam snapshots
License:        BSD-2-Clause
URL:            https://github.com/matwey/django-eremaea2
Source:         https://files.pythonhosted.org/packages/source/d/django-eremaea2/django_eremaea2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  %{python_module cmdln}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module django-dj-inmemorystorage}
BuildRequires:  %{python_module djangorestframework >= 3.7.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
# https://github.com/matwey/django-eremaea2/issues/15
BuildRequires:  %{python_module python-magic}
BuildRequires:  %{python_module requests-mock}
# https://github.com/matwey/django-eremaea2/issues/15
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       eremaea = %{version}
Requires:       python-cmdln
Requires:       python-djangorestframework >= 3.7.0
Requires:       python-python-magic
Requires:       python-requests
Requires:       python-requests-toolbelt
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
django-eremaea2 is a simple Django application to store and manage webcam image snapshots.
The application is built on top of django-rest-framework and provides REST API to access the files.

%package -n eremaea
Summary:        Systemd unit files for python-django-eremaea2
Group:          Development/Languages/Python
Requires:       /usr/bin/eremaeactl
%{?systemd_ordering}

%description -n eremaea
This package contains the systemd unit files for python-django-eremaea2.

%prep
%autosetup -p1 -n django_eremaea2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/eremaeactl

install -D -m 0644 eremaea-purge@.timer   %{buildroot}%{_unitdir}/eremaea-purge@.timer
install -D -m 0644 eremaea-purge@.service %{buildroot}%{_unitdir}/eremaea-purge@.service
install -D -m 0644 eremaea-pull@.service  %{buildroot}%{_unitdir}/eremaea-pull@.service
install -D -m 0644 eremaea.target         %{buildroot}%{_unitdir}/eremaea.target
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rceremaea

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$(pwd)
%pytest

%post
%python_install_alternative eremaeactl

%postun
%python_uninstall_alternative eremaeactl

%pre -n eremaea
%service_add_pre eremaea.target

%post -n eremaea
%service_add_post eremaea.target

%preun -n eremaea
%service_del_preun eremaea.target

%postun -n eremaea
%service_del_postun eremaea.target

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/eremaeactl
%{python_sitelib}/*eremaea*

%files -n eremaea
%defattr(-,root,root,-)
%license LICENSE
%{_unitdir}/eremaea-purge@.timer
%{_unitdir}/eremaea-purge@.service
%{_unitdir}/eremaea-pull@.service
%{_unitdir}/eremaea.target
%{_sbindir}/rceremaea

%changelog
