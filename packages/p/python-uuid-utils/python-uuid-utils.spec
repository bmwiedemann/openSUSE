#
# spec file for package python-uuid-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-uuid-utils
Version:        0.14.1
Release:        0
Summary:        Fast, drop-in replacement for Python's uuid module, powered by Rust
License:        BSD-3-Clause
URL:            https://github.com/aminalaee/uuid-utils
Source0:        https://files.pythonhosted.org/packages/source/u/uuid-utils/uuid_utils-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-uuid_utils = %{version}-%{release}
%python_subpackages

%description
Fast, drop-in replacement for Python's uuid module, powered by Rust.

Available UUID versions:

- uuid1 - Version 1 UUIDs using a timestamp and monotonic counter.
- uuid3 - Version 3 UUIDs based on the MD5 hash of some data.
- uuid4 - Version 4 UUIDs with random data.
- uuid5 - Version 5 UUIDs based on the SHA1 hash of some data.
- uuid6 - Version 6 UUIDs using a timestamp and monotonic counter.
- uuid7 - Version 7 UUIDs using a Unix timestamp ordered by time.
- uuid8 - Version 8 UUIDs using user-defined data.

%prep
%autosetup -p1 -a1 -n uuid_utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -k 'not (test_reseed_is_called_when_forking or test_getnode)'

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitearch}/uuid_utils
%{python_sitearch}/uuid_utils-%{version}.dist-info

%changelog
