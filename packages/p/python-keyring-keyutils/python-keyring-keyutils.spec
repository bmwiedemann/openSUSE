#
# spec file for package python-keyring-keyutils
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
Name:           python-keyring-keyutils
Version:        0.1.1
Release:        0
Summary:        A python-keyring backend for the kernel keyring
License:        MIT
URL:            https://github.com/marcus-h/python-keyring-keyutils
Source:         keyring-keyutils-%{version}.tar.gz
# PATCH-FIX-UPSTREAM keyring-util-properties.patch gh#jaraco/keyring#593 mcepl@suse.com
# this patch makes things totally awesome
Patch0:         keyring-util-properties.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  keyutils-devel
BuildRequires:  python-rpm-macros

%python_subpackages

%description
A python-keyring [1] backend that can be used to access the kernel
keyring. In particular, this package ships

- a python-keyring [1] backend for the kernel keyring
- a special python-keyring backend that can be used by osc
- a high-level interface to the kernel keyring
- a low-level module that wraps around the C keyutils library [2]

[1] https://github.com/jaraco/keyring
[2] https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git

%prep
%autosetup -p1 -n keyring-keyutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The test_key_too_large_serial testcase only makes sense if int32_t and long
# have different ranges of values
cat > skip_test_key_too_large_serial.c <<'EOF'
#include <stdint.h>

int main(void) {
    return sizeof(int32_t) != sizeof(long);
}
EOF
gcc -Wall -o skip_test_key_too_large_serial skip_test_key_too_large_serial.c

./skip_test_key_too_large_serial && SKIP=(-k 'not test_key_too_large_serial')
%pytest_arch "${SKIP[@]}" tests

%files %{python_files}
%doc README.md README_osc.md
%license LICENSE
%{python_sitearch}/keyutils
%{python_sitearch}/keyring_keyutils-%{version}*-info

%changelog
