#
# spec file for package python3-ec2metadata
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


%{?sle15_python_module_pythons}
%define upstream_name ec2metadata
Name:           python-ec2metadata
Version:        5.0.0
Release:        0
Summary:        Collect instance metadata in EC2
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/ec2metadata
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Obsoletes:      python3-ec2metadata <= %{version}
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Collect instance meta data in Amazon Compute CLoud instances

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/ec2metadata.1 %{buildroot}/%{_mandir}/man1
%python_clone -a %{buildroot}%{_bindir}/%{upstream_name}
%python_clone -a %{buildroot}%{_mandir}/man1/ec2metadata.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ec2metadata ec2metadata.1%{?ext_man}

%postun
%python_uninstall_alternative ec2metadata

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/%{upstream_name}
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}*-info
%python_alternative %{_mandir}/man1/%{upstream_name}.1%{?ext_man}

%changelog
