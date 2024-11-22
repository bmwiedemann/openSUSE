#
# spec file for package python-fastavro
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


%{?sle15_python_module_pythons}
Name:           python-fastavro
Version:        1.9.7
Release:        0
Summary:        Fast read/write of AVRO files
License:        MIT
# gh#fastavro/fastavro#526 … doesn’t work on 32bit
ExcludeArch:    %{ix86}
URL:            https://github.com/fastavro/fastavro
Source:         https://files.pythonhosted.org/packages/source/f/fastavro/fastavro-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-cramjam
Suggests:       python-lz4
Suggests:       python-zstandard
# SECTION test requirements
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zlib-ng}
BuildRequires:  %{python_module zstandard}
# /SECTION
%python_subpackages

%description
Fast read/write of AVRO files

%prep
%setup -q -n fastavro-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/fastavro
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
donttest="test_optional_codecs[snappy]"
donttest+=" or test_optional_codecs_not_installed_reading[snappy]"
%pytest -k "not ($donttest)"

%post
%python_install_alternative fastavro

%postun
%python_uninstall_alternative fastavro

%files %{python_files}
%doc ChangeLog README.md
%license LICENSE
%python_alternative %{_bindir}/fastavro
%{python_sitearch}/fastavro
%{python_sitearch}/fastavro-%{version}*-info

%changelog
