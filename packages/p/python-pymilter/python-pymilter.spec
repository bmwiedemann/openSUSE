#
# spec file for package python-pymilter
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pymilter
Version:        1.0.5
Release:        0
Summary:        Python interface to the sendmail milter API
License:        GPL-2.0-or-later
URL:            https://www.bmsi.com/python/milter.html
Source0:        https://github.com/sdgathman/pymilter/archive/pymilter-%{version}.tar.gz
Source1:        tmpfiles-python-pymilter.conf
# PATCH-FIX-UPSTREAM: https://github.com/sdgathman/pymilter/pull/57
Patch1:         0001-Remove-calls-to-the-deprecated-method-assertEquals.patch
# PATCH-FIX-UPSTREAM https://github.com/sdgathman/pymilter/pull/70
Patch2:         set-c-standard-17.patch
BuildRequires:  %{python_module bsddb3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sendmail-devel >= 8.13
BuildRequires:  systemd-rpm-macros
# Common subpackage named as such to avoid creating flavor packages
Requires:       pymilter-common = %{version}-%{release}
Requires:       python
Requires:       python-bsddb3
Requires:       python-py3dns
%python_subpackages

%description
This is a Python extension module to enable python scripts to attach to
sendmail's libmilter functionality. Additional Python modules provide for
navigation and modification of MIME parts, sending DSNs, and doing CBV.

%package -n pymilter-common
Summary:        Common files for pymilter
Requires(post): systemd
BuildArch:      noarch

%description -n pymilter-common
This package contains the common files used for pymilter.

%prep
%autosetup -n pymilter-pymilter-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_localstatedir}/log/milter
mkdir -p %{buildroot}%{_libexecdir}/milter
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%python_expand %fdupes %{buildroot}/%{$python_sitearch}

%check
# remove tests that don't work
rm test.py testpolicy.py
%pyunittest_arch -v

%files %{python_files}
%doc README.md ChangeLog NEWS TODO CREDITS sample.py template.py
%license COPYING
%{python_sitearch}/Milter
%{python_sitearch}/milter.cpython*
%{python_sitearch}/mime.py
%{python_sitearch}/pymilter-%{version}*-info
%pycache_only %{python_sitearch}/__pycache__/mime*

%files -n pymilter-common
%license COPYING
%{_libexecdir}/milter
%dir %attr(0755,mail,mail) %{_localstatedir}/log/milter
%{_tmpfilesdir}/%{name}.conf

%post -n pymilter-common
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%changelog
