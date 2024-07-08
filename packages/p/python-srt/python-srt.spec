#
# spec file for package python-srt
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


Name:           python-srt
Version:        3.5.3
Release:        0
Summary:        Python library for handling SRT files, plus tools
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cdown/srt
Source0:        https://files.pythonhosted.org/packages/source/s/srt/srt-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
srt is a Python library for parsing, modifying, and composing SRT files.

It also includes related tools.

%prep
%autosetup -p1 -n srt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/srt
%python_clone -a %{buildroot}%{_bindir}/srt-deduplicate
%python_clone -a %{buildroot}%{_bindir}/srt-fixed-timeshift
%python_clone -a %{buildroot}%{_bindir}/srt-linear-timeshift
%python_clone -a %{buildroot}%{_bindir}/srt-lines-matching
%python_clone -a %{buildroot}%{_bindir}/srt-mux
%python_clone -a %{buildroot}%{_bindir}/srt-normalise
%python_clone -a %{buildroot}%{_bindir}/srt-play
%python_clone -a %{buildroot}%{_bindir}/srt-process

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative srt
%python_install_alternative srt-deduplicate
%python_install_alternative srt-fixed-timeshift
%python_install_alternative srt-linear-timeshift
%python_install_alternative srt-lines-matching
%python_install_alternative srt-mux
%python_install_alternative srt-normalise
%python_install_alternative srt-play
%python_install_alternative srt-process

%postun
%python_uninstall_alternative srt
%python_uninstall_alternative srt-deduplicate
%python_uninstall_alternative srt-fixed-timeshift
%python_uninstall_alternative srt-linear-timeshift
%python_uninstall_alternative srt-lines-matching
%python_uninstall_alternative srt-mux
%python_uninstall_alternative srt-normalise
%python_uninstall_alternative srt-play
%python_uninstall_alternative srt-process

%check
# online tests only

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/srt
%python_alternative %{_bindir}/srt-deduplicate
%python_alternative %{_bindir}/srt-fixed-timeshift
%python_alternative %{_bindir}/srt-linear-timeshift
%python_alternative %{_bindir}/srt-lines-matching
%python_alternative %{_bindir}/srt-mux
%python_alternative %{_bindir}/srt-normalise
%python_alternative %{_bindir}/srt-play
%python_alternative %{_bindir}/srt-process
%pycache_only %{python_sitelib}/__pycache__/srt.cpython-%{python_version_nodots}*
%{python_sitelib}/srt.py
%{python_sitelib}/srt_tools
%{python_sitelib}/srt-%{version}.dist-info

%changelog
