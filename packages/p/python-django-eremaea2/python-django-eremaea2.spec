#
# spec file for package python-django-eremaea2
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


%define skip_python2 1
Name:           python-django-eremaea2
Version:        2.0.18
Release:        0
Summary:        A simple Django application to store and show webcam snapshots
License:        BSD-2-Clause
URL:            https://github.com/matwey/django-eremaea2
Source:         https://files.pythonhosted.org/packages/source/d/django-eremaea2/django-eremaea2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  %{python_module Django >= 1.10}
BuildRequires:  %{python_module cmdln}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module django-dj-inmemorystorage}
BuildRequires:  %{python_module djangorestframework >= 3.7.0}
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
Requires:       python-Django >= 1.10
Requires:       python-cmdln
Requires:       python-djangorestframework >= 3.7.0
Requires:       python-magic
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
%autosetup -p1 -n django-eremaea2-%{version}

%build
%python_build

%install
%python_install

for p in eremaeactl ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

for u in eremaea-purge@.timer eremaea-purge@.service eremaea-pull@.service eremaea.target ; do
    install -D -m 0644 $u %{buildroot}%{_unitdir}/$u
done
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rceremaea

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.test_settings
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
