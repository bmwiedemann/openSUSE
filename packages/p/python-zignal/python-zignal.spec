#
# spec file for package python-zignal
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-zignal
Version:        0.6.0
Release:        0
Summary:        Audio signal processing library
License:        MIT
URL:            https://github.com/ronnyandersson/zignal
Source:         https://github.com/ronnyandersson/zignal/archive/%{version}.tar.gz#/zignal-%{version}.tar.gz
# PACH-FIX-OPENSUSE numpy-1.24.patch gh#ronnyandersson/zignal#11
Patch0:         numpy-1.24.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-samplerate
Requires:       python-scipy
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-PyAudio
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module samplerate}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
This is a python audio signal processing library.

%prep
%autosetup -p1 -n zignal-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/zignal-listsndcards
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/ronnyandersson/zignal/issues/9
sed -i '/import nose/d' zignal/tests/*.py
# https://github.com/ronnyandersson/zignal/issues/8
%pytest -k 'not test_set_duration_and_samples'

%post
%python_install_alternative zignal-listsndcards

%postun
%python_uninstall_alternative zignal-listsndcards

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/zignal-listsndcards
%{python_sitelib}/zignal
%{python_sitelib}/zignal-%{version}*-info

%changelog
