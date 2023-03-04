#
# spec file for package python-urlgrabber
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


%define modname urlgrabber
Name:           python-urlgrabber
Version:        4.1.0
Release:        0
Summary:        A high-level cross-protocol url-grabber
License:        LGPL-2.1-only
Group:          Development/Libraries/Python
URL:            https://github.com/rpm-software-management/urlgrabber
Source:         https://github.com/rpm-software-management/%{modname}/releases/download/%{modname}-4-1-0/%{modname}-%{version}.tar.gz
# PATCH-FIX_UPSTREAM gh#rpm-software-management/urlgrabber!32
Patch0:         use-binary-mode-when-reopening-files.patch
# PATCH-FIX_UPSTREAM gh#rpm-software-management/urlgrabber!35
Patch1:         fix_find_proxy_logic_and_drop_six.patch
# PATCH-FIX_UPSTREAM gh#rpm-software-management/urlgrabber!34
Patch2:         avoid_crashing_when_urlgrabber_debug_enabled.patch
# PATCH-FIX_UPSTREAM gh#rpm-software-management/urlgrabber!37
Patch3:         fix-urlgrab-file-schema-comparison.patch

BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycurl
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A high-level cross-protocol url-grabber for python supporting HTTP, FTP
and file locations.  Features include keepalive, byte ranges,
throttling, authentication, proxies and more.

%prep
%setup -q -n urlgrabber-%{version}
# Remove with next release
sed -i "13d" urlgrabber/__init__.py # Remove wrong license header, fixes bnc#781323
%autopatch -p1

# Fix location of %%{_libexecdir}
sed -i 's!/usr/libexec!%{_libexecdir}!' urlgrabber/grabber.py
sed -i "s!libexec!$(echo %{_libexecdir}|cut -d/ -f 3)!" setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/urlgrabber
%python_clone -a %{buildroot}%{_libexecdir}/urlgrabber-ext-down
rm -rf %{buildroot}%{_datadir}/doc/urlgrabber-%{version} # Remove wrongly installed docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative urlgrabber
%{python_expand %{_sbindir}/update-alternatives --quiet --install %{_libexecdir}/urlgrabber-ext-down  urlgrabber-ext-down   %{_libexecdir}/urlgrabber-ext-down-%{$python_version}  %{$python_version_nodots}}

%postun
%python_uninstall_alternative urlgrabber
if [ ! -f %{_libexecdir}/urlgrabber-ext-down ] ; then
   update-alternatives --remove urlgrabber-ext-down %{_libexecdir}/urlgrabber-ext-down
fi

%files %{python_files}
%license LICENSE
%doc ChangeLog README TODO
%python_alternative %{_bindir}/urlgrabber
%python_alternative %{_libexecdir}/urlgrabber-ext-down
%{python_sitelib}/urlgrabber
%{python_sitelib}/urlgrabber-%{version}*-info

%changelog
