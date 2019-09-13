#
# spec file for package python-pymilter
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


# we don't want to provide private python extension libs
%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so|%{python3_sitearch}/.*\\.so)$

# Python 2 module isn't building properly and we don't really need it right now anyway...
%global skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Summary:        Python interface to the sendmail milter API
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
Name:           python-pymilter
Version:        1.0.4
Release:        0
URL:            http://www.bmsi.com/python/milter.html
Source0:        https://github.com/sdgathman/pymilter/archive/pymilter-%{version}.tar.gz
Source1:        tmpfiles-python-pymilter.conf
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sendmail-devel >= 8.13
BuildRequires:  systemd-rpm-macros
%if "%{python_flavor}" == "python2"
Requires:       python2-pydns
%endif
%if "%{python_flavor}" == "python3"
Requires:       python3-py3dns
%endif
# Common subpackage named as such to avoid creating flavor packages
Requires:       pymilter-common = %{version}-%{release}
%python_subpackages

%description
This is a Python extension module to enable python scripts to attach to
sendmail's libmilter functionality. Additional Python modules provide for
navigation and modification of MIME parts, sending DSNs, and doing CBV.

%package -n pymilter-common
Summary:        Common files for pymilter
Group:          Development/Languages/Python
BuildArch:      noarch
Requires(post): systemd

%description -n pymilter-common
This package contains the common files used for pymilter.

%prep
%autosetup -n pymilter-pymilter-%{version} -p1

%build
%python_build

%install
%python_install

mkdir -p %{buildroot}%{_localstatedir}/log/milter
mkdir -p %{buildroot}%{_libexecdir}/milter
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%fdupes %{buildroot}%{python_sitearch}/*

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m unittest discover
}

%files %{python_files}
%doc README ChangeLog NEWS TODO CREDITS sample.py milter-template.py
%license COPYING
%{python_sitearch}/*

%files -n pymilter-common
%license COPYING
%{_libexecdir}/milter
%dir %attr(0755,mail,mail) %{_localstatedir}/log/milter
%{_tmpfilesdir}/%{name}.conf

%post -n pymilter-common
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%changelog
