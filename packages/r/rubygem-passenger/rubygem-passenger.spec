#
# spec file for package rubygem-passenger
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-passenger
Version:        6.0.22
Release:        0
%define mod_name passenger
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} > 1220
%bcond_without systemd
%define passenger_tempdir /run/passenger
%else
%bcond_with    systemd
%define passenger_tempdir /var/run/passenger
%endif
%bcond_without systemlibs
BuildRequires:  apache2-devel
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
%if 0%{?suse_version} >= 1110
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif
BuildRequires:  zlib-devel
%if %{with systemlibs}
#BuildRequires:  libeio-devel
#BuildRequires:  libev-devel
%endif
BuildRequires:  %{rubygem rake}
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-utils
# TODO: move to subpackage
Recommends:     packageand(apache2:rubygem-passenger-apache2)
Recommends:     packageand(nginx:rubygem-passenger-nginx)
Requires:       rubygem(passenger) = %{version}
Recommends:     rubygem(%{rb_default_ruby_abi}:passenger) = %{version}
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
URL:            https://www.phusionpassenger.com/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        mod_passenger.conf
Source2:        mod_passenger_root.include
Source3:        nginx_passenger.conf
Source4:        nginx_passenger_root.include
Source5:        passenger.systemd.conf
Source6:        series
Source7:        rubygem-passenger-rpmlintrc
Source8:        gem2rpm.yml
# MANUAL
Patch0:         0001-suse.patch
Patch1:         0002-fix-shebangs.patch
# /MANUAL
Summary:        A fast and robust web server and application server for Ruby, Python
License:        GPL-2.0-only AND MIT
PreReq:         update-alternatives

%description
A modern web server and application server for Ruby, Python and Node.js,
optimized for performance, low memory usage and ease of use.

%prep
%gem_unpack
%patch -P 0 -p1
%patch -P 1 -p1
# MANUAL
# those files have been committed accidentally by the developers of passenger with version 6.0.8. they are not needed so
# we have to remove them (otherwise a suse-filelist-forbidden linter error with a badness of 10000 is raised when .orig
# files are in the file list). Patching src/ruby_supportlib/phusion_passenger/packaging.rb to exclude these files from
# the packaging process did not work out, because it's getting parsed before the patch even applies.
# If you find a better solution, feel free to improve this section here.
#
# The files will probably be removed with a later release, so feel free to drop this section if the building fails
# because of those files being missing.
sed -i 's/"src\/cxx_supportlib\/vendor-modified\/boost\/thread\/detail\/thread.hpp.orig".freeze, //g' passenger-*.gemspec
sed -i 's/"src\/cxx_supportlib\/vendor-modified\/boost\/thread\/once.hpp.orig".freeze, //g' passenger-*.gemspec
# Do not install a Python script with +x
chmod a-x src/cxx_supportlib/vendor-copy/libuv/gyp_uv.py
# /MANUAL
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
# MANUAL
# TODO:
# currently -lev gets lost when using system libev
%if %{with systemlibs}
export USE_VENDORED_LIBEV="yes"
export USE_VENDORED_LIBEIO="yes"
%endif
# /MANUAL
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG LICENSE README.md" \
  -f
%gem_cleanup
# MANUAL
# avoid BUILDROOT leaking into the binaries
pushd %{mod_full_name}
  export PATH="%{_sbindir}:$PATH"

  #compiling nginx stuff
  rake nginx:clean nginx CACHING=no

  #compiling apache2 stuff
  rake apache2 CACHING="no"
  install -D -m 0755 buildout/apache2/mod_passenger.so %{buildroot}%{apache_libexecdir}/mod_passenger.so

  for i in $(/usr/bin/ruby-find-versioned) ; do
    rubysuffix="${i#/usr/bin/ruby}"
    /usr/bin/rake$rubysuffix native_support
    # we dont calculate the arch here as passenger build seems to use the running host arch and not the arch that ruby was build with.
    rubydir=$($i -r rubygems -e 'puts "#{Gem.ruby_engine}-#{RUBY_VERSION}-"')
    gemdir="%{buildroot}$(/usr/bin/gem$rubysuffix env gemdir)/gems/%{mod_full_name}/src/ruby_supportlib/"
    cp -v buildout/ruby/$rubydir*/*.so $gemdir
    /usr/bin/rake$rubysuffix native_support:clean
  done
  find buildout -name \*.o -print -delete
  mkdir -p %{buildroot}%{_libdir}/passenger/%{version}/{buildout,src}/
  cp -av buildout/support-binaries/                                 %{buildroot}%{_libdir}/passenger/%{version}/
  cp -av src/nodejs_supportlib/ src/helper-scripts/ bin/ resources/ %{buildroot}%{_libdir}/passenger/%{version}/
popd
#
#
#
mkdir -p %{buildroot}%{_sysconfdir}/passenger/
cat <<EOF >  %{buildroot}%{_sysconfdir}/passenger/locations.ini
[locations]
packaging_method=rpm
natively_packaged=true
bin_dir=%{_libdir}/passenger/%{version}/bin/
support_binaries_dir=%{_libdir}/passenger/%{version}/support-binaries/
lib_dir=%{_libdir}/passenger/%{version}/
include_dir=%{_libdir}/passenger/%{version}/
helper_scripts_dir=%{_libdir}/passenger/%{version}/helper-scripts/
node_libdir=%{_libdir}/passenger/%{version}/nodejs_supportlib/
resources_dir=%{_libdir}/passenger/%{version}/resources/
apache2_module_path=%{apache_libexecdir}/mod_passenger.so
ruby_libdir=%{_libdir}/passenger/%{version}/ignore
ruby_extension_source_dir=%{_libdir}/passenger/%{version}/ignore
nginx_module_source_dir=%{_libdir}/passenger/%{version}/ignore
doc_dir=%{_libdir}/passenger/%{version}/ignore
EOF

# webserver configs
install -D -m 0644 %{S:1} %{buildroot}%{apache_sysconfdir}/conf.d/mod_passenger.conf
install -D -m 0644 %{S:2} %{buildroot}%{apache_sysconfdir}/conf.d/mod_passenger_root.include
install -D -m 0644 %{S:3} %{buildroot}/etc/nginx/conf.d/passenger.conf
install -D -m 0644 %{S:4} %{buildroot}/etc/nginx/conf.d/passenger_root.include
#
sed -i -e "s,@passengertmpdir@,%{passenger_tempdir},"           %{buildroot}%{apache_sysconfdir}/conf.d/mod_passenger.conf
sed -i -e "s,@PassengerRoot@,%{_libdir}/passenger/%{version}/," %{buildroot}%{apache_sysconfdir}/conf.d/mod_passenger_root.include

sed -i -e "s,@passengertmpdir@,%{passenger_tempdir},"           %{buildroot}/etc/nginx/conf.d/passenger.conf
sed -i -e "s,@PassengerRoot@,%{_libdir}/passenger/%{version}/," %{buildroot}/etc/nginx/conf.d/passenger_root.include
#
%if %{with systemd}
install -D -m 0644 %{S:5} %{buildroot}/usr/lib/tmpfiles.d/passenger.conf
%endif
# /MANUAL

%files
%defattr(-,root,root,-)
%if %{with systemd}
/usr/lib/tmpfiles.d/passenger.conf
%endif
%config %{_sysconfdir}/passenger/
%dir %{_libdir}/passenger/
%{_libdir}/passenger/%{version}/

%post
%if %{with systemd}
systemd-tmpfiles --create /usr/lib/tmpfiles.d/passenger.conf || true
%endif

%package apache2
Requires:       %{apache_mmn}
Requires:       apache2
Requires:       rubygem-passenger = %{version}
Summary:        Passenger apache module
Group:          Development/Languages/Ruby
Supplements:    packageand(apache2:rubygem-passenger)

# Requires:      rubygem-passenger = 6.0.22
%description apache2

A modern web server and application server for Ruby, Python and Node.js,
optimized for performance, low memory usage and ease of use.

This package holds the apache2 sub package for passenger

%files apache2
%defattr(-,root,root,-)
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_passenger.conf
%config            %{apache_sysconfdir}/conf.d/mod_passenger_root.include
%{apache_libexecdir}/mod_passenger.so

%package nginx
Requires:       nginx
Requires:       rubygem-passenger = %{version}
Summary:        Passenger Nginx module
Group:          Development/Languages/Ruby
Supplements:    packageand(nginx:rubygem-passenger)

# Requires:      rubygem-passenger = 6.0.22
%description nginx

A modern web server and application server for Ruby, Python and Node.js,
optimized for performance, low memory usage and ease of use.

This package holds the nginx sub package for passenger

%files nginx
%defattr(-,root,root,-)
%dir /etc/nginx/
%dir /etc/nginx/conf.d/
%config(noreplace) /etc/nginx/conf.d/passenger.conf
%config            /etc/nginx/conf.d/passenger_root.include

%gem_packages

%changelog
