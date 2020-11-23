#
# spec file for package yast2-ruby-bindings
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-ruby-bindings
Version:        4.3.11
Release:        0
URL:            https://github.com/yast/yast-ruby-bindings
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-ruby-bindings-%{version}.tar.bz2
Prefix:         /usr

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10
%if 0%{?suse_version} == 1310
BuildRequires:  rubygem-fast_gettext < 3.0
BuildRequires:  rubygem-rspec
Requires:       rubygem-fast_gettext < 3.0
%else
BuildRequires:  rubygem(%{rb_default_ruby_abi}:fast_gettext) < 3.0
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
Requires:       rubygem(%{rb_default_ruby_abi}:fast_gettext) < 3.0
%endif
BuildRequires:  ruby-devel
Requires:       yast2-core >= 3.2.2
BuildRequires:  yast2-core-devel >= 3.2.2
# MenuBar-shortcuts-test.rb
Requires:       yast2-ycp-ui-bindings       >= 4.3.7
BuildRequires:  yast2-ycp-ui-bindings-devel >= 4.3.7
# The test suite includes a regression test (std_streams_spec.rb) for a
# libyui-ncurses bug fixed in 2.47.3
BuildRequires:  libyui-ncurses >= 2.47.3
# The mentioned test requires tmux in order to be executed in headless systems
# Also many other libyui tests to come
BuildRequires:  tmux

# only a soft dependency, the Ruby debugger is optional
Suggests:       rubygem(%{rb_default_ruby_abi}:byebug)

# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake-ci)
%endif

Requires:       ruby
Summary:        Ruby bindings for the YaST platform
License:        GPL-2.0-only
Group:          System/YaST

%description
The bindings allow YaST modules to be written using the Ruby language
and also Ruby scripts can use YaST agents, APIs and modules.

%prep
%setup -n yast2-ruby-bindings-%{version}
%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make %{?jobs:-j %jobs} VERBOSE=1

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT
cd -

%check
# Build workers are set up without systemd so the default /run/tmux dir
# will not be present (unless clamav pulls systemd in, on SLE)
export TMUX_TMPDIR=/tmp
cd build
make test ARGS=-V
cd -

# run extra CI checks (in Jenkins)
%if %{with yast_run_ci_tests}
%yast_ci_check
%endif

%files
%defattr (-, root, root)
%{yast_ybindir}/y2start
%{_libdir}/YaST2/plugin/libpy2lang_ruby.so
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/*.rb
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/yast
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/*x.so
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/yast
%license COPYING

%changelog
