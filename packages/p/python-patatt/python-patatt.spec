#
# spec file for package python-patatt
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-patatt
Version:        0.6.3
Release:        0
Summary:        Cryptographic patch attestation for the masses
License:        MIT-0
URL:            https://git.kernel.org/pub/scm/utils/patatt/patatt.git/
Source0:        https://git.kernel.org/pub/scm/utils/patatt/patatt.git/snapshot/patatt-%{version}.tar.gz
Source1:        https://git.kernel.org/pub/scm/utils/patatt/patatt.git/snapshot/patatt-%{version}.tar.asc
Source2:        python-patatt.keyring
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  git-core
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
This utility allows an easy way to add end-to-end cryptographic attestation to
patches sent via mail. It does so by adapting the DKIM email signature standard
to include cryptographic signatures via the X-Developer-Signature email header.

If your project workflow doesn't use patches sent via email, then you don't
need this and should simply start signing your tags and commits.

%prep
%autosetup -n patatt-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/patatt
%python_clone -a %{buildroot}%{_mandir}/man5/patatt.5

%check
# try at least a simple runtime test
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" %{buildroot}%{_bindir}/patatt-%{$python_bin_suffix} --version | grep -q %{version}

%post
%{python_install_alternative patatt patatt.5}

%postun
%python_uninstall_alternative patatt

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/patatt
%python_alternative %{_mandir}/man5/patatt.5%{?ext_man}
%{python_sitelib}/*

%changelog
