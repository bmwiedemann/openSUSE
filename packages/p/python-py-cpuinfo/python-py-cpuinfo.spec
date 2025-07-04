#
# spec file for package python-py-cpuinfo
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without tests
%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-py-cpuinfo
Version:        9.0.0
Release:        0
Summary:        Python library and tool to get CPU info
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/workhorsy/py-cpuinfo
Source:         https://files.pythonhosted.org/packages/source/p/py-cpuinfo/py-cpuinfo-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS
provides. It supports Linux, OS X, Windows, BSD, Solaris,
Cygwin, Haiku, and BeagleBone, but only on x86 and some ARM CPUs.

These approaches are used for getting info:
 1. Windows Registry (Windows)
 2. /proc/cpuinfo (Linux)
 3. sysctl (OS X)
 4. dmesg (Unix/Linux)
 5. isainfo and kstat (Solaris)
 6. cpufreq-info (BeagleBone)
 7. lscpu (Unix/Linux)
 8. sysinfo (Haiku)
 9. Querying the CPUID register (Intel X86 CPUs)

%prep
%setup -q -n py-cpuinfo-%{version}
# remove shebang
sed -i '1{ /^#!/d; }' cpuinfo/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare for alts usage
%python_clone -a %{buildroot}%{_bindir}/cpuinfo

%if %{with tests}
%check
%python_exec test_suite.py
%endif

%pre
%python_libalternatives_reset_alternative cpuinfo

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%python_alternative %{_bindir}/cpuinfo
%{python_sitelib}/cpuinfo
%{python_sitelib}/py_cpuinfo-%{version}*-info

%changelog
