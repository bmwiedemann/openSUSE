#
# spec file for package python-trio
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-trio
Version:        0.22.0
Release:        0
Summary:        Python async/await-native I/O library
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trio
Source:         https://files.pythonhosted.org/packages/source/t/trio/trio-%{version}.tar.gz
BuildRequires:  %{python_module astor >= 0.8}
BuildRequires:  %{python_module async_generator >= 1.9}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module exceptiongroup >= 1.0.0~rc9 if %python-base < 3.11}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module outcome}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module setuptools}
# for protocol specifications
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module yapf >= 0.27.0}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-async_generator >= 1.9
Requires:       python-attrs >= 19.2.0
%if 0%{?python_version_nodots} < 311
Requires:       python-exceptiongroup >= 1.0.0~rc9
%endif
Requires:       python-idna
Requires:       python-outcome
Requires:       python-sniffio
Requires:       python-sortedcontainers
BuildArch:      noarch
%python_subpackages

%description
The Trio project produces an async/await-native I/O library for
Python. Like all async libraries, its main purpose is to help write
programs that do multiple things at the same time with parallelized
I/O, such as a web spider that wants to fetch lots of pages in
parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor
monitoring multiple subprocesses. Compared to other libraries, Trio
has an obsessive focus on usability and correctness.

%prep
%autosetup -p1 -n trio-%{version}
sed -i '1{/^#!/d}' trio/_tools/gen_exports.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/trio/{,_core/}tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# test_static_tool_sees_all_symbols uses jedi/pylint for static analysis,
#   pointless for us.
# test_SSLStream_generic deadlocks in OBS
# test_close_at_bad_time_for_send_all fails on PPC https://github.com/python-trio/trio/issues/1753
# test_local_address_real fails on qemu_linux_user targets
%pytest -k 'not (test_static_tool_sees_all_symbols or test_SSLStream_generic or test_close_at_bad_time_for_send_all or test_local_address_real)'

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/trio
%{python_sitelib}/trio-%{version}*-info

%changelog
