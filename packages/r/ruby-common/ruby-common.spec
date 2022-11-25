#
# spec file for package ruby-common
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


### seems that %{_rpmmacrodir} is not known on SLE 12 / Leap 42
%if 0%{?suse_version} == 1315
%define _rpmmacrodir /etc/rpm
%endif

Name:           ruby-common
Version:        3.2
Release:        0
# ruby-macros and ruby-common version
%define rpm_macros_version 5
%if 0
%bcond_with    ship_gemrc
%else
%bcond_without ship_gemrc
%endif
Source1:        gem_build_cleanup
Source2:        gemrc
Source4:        rubygems.attr
Source5:        rubygemsdeps.rb
Source6:        gem_install.sh
Source7:        generate_buildrequires.sh
Source8:        ruby-common.macros
Source9:        ruby.rpm-macros
Source10:       gem_packages.sh
Source11:       gem_packages.spec.erb
Source12:       ruby-find-versioned
Source13:       gemfile.attr
Source14:       gemfile.rb
Source15:       rails.macros
Source16:       g2r
Source17:       rubygems_bundled.attr
Summary:        Collection of scripts and macros for ruby packaging
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/openSUSE/ruby-packaging/
Requires:       /usr/bin/getopt
Requires:       rubygem(gem2rpm)
Recommends:     rubygem(%{rb_default_ruby_abi}:gem2rpm)
Requires:       fdupes
BuildArch:      noarch
Provides:       ruby-macros = %{rpm_macros_version}
%if 0%{?suse_version} < 1140 && 0%{?suse_version} > 1110
# we need a patched rpm
Requires:       rpm-with-ruby-provide-hook
%endif

%description
This package is needed for (generated) ruby gems. It provides hooks for
automatic rpm provides and requires and macros that gem2rpm uses.

%package rails
Requires:       rubygem(bundler)
Recommends:     rubygem(%{rb_default_ruby_abi}:bundler)
Requires:       %{name} = %{version}-%{release}

Summary:        Rails packaging support
Group:          Development/Languages/Ruby

%description rails
This package is needed for (generated) ruby gems. It provides hooks for
automatic rpm provides and requires and macros that gem2rpm uses.

Rails packaging support files.

%prep

%build

%install
# we need to make sure it overwrites older macro versions and rpm sorts alphabetically
%if %{with ship_gemrc}
install -D -m 0644 %{S:2}  %{buildroot}/etc/gemrc
%endif
install -D -m 0644 %{S:8}  %{buildroot}%{_rpmmacrodir}/macros.ruby-common
install -D -m 0644 %{S:9}  %{buildroot}%{_rpmmacrodir}/macros.suse-ruby
install -D -m 0644 %{S:4}  %{buildroot}/usr/lib/rpm/fileattrs/rubygems.attr
install -D -m 0755 %{S:5}  %{buildroot}/usr/lib/rpm/rubygemsdeps.rb
install -D -m 0755 %{S:6}  %{buildroot}/usr/lib/rpm/gem_install.sh
install -D -m 0755 %{S:1}  %{buildroot}/usr/lib/rpm/gem_build_cleanup.sh
install -D -m 0755 %{S:7}  %{buildroot}/usr/lib/rpm/generate_buildrequires.sh
install -D -m 0755 %{S:10} %{buildroot}/usr/lib/rpm/gem_packages.sh
install -D -m 0644 %{S:11} %{buildroot}/usr/lib/rpm/gem_packages.template
install -D -m 0755 %{S:12} %{buildroot}%{_bindir}/ruby-find-versioned
install -D -m 0644 %{S:13} %{buildroot}/usr/lib/rpm/fileattrs/gemfile.attr
install -D -m 0755 %{S:14} %{buildroot}/usr/lib/rpm/gemfile.rb
install -D -m 0644 %{S:15} %{buildroot}%{_rpmmacrodir}/macros.rails
install -D -m 0755 %{S:16} %{buildroot}%{_bindir}/g2r
install -D -m 0644 %{S:17} %{buildroot}/usr/lib/rpm/fileattrs/rubygems_bundled.attr

%files
%defattr(-,root,root)
%if %{with ship_gemrc}
%config /etc/gemrc
%endif
%{_rpmmacrodir}/macros.*ruby*
%dir /usr/lib/rpm/fileattrs
/usr/lib/rpm/fileattrs/rubygems.attr
/usr/lib/rpm/fileattrs/rubygems_bundled.attr
/usr/lib/rpm/rubygemsdeps.rb
/usr/lib/rpm/gem_install.sh
/usr/lib/rpm/gem_build_cleanup.sh
/usr/lib/rpm/generate_buildrequires.sh
/usr/lib/rpm/gem_packages.*
%{_bindir}/ruby-find-versioned
%{_bindir}/g2r

%files rails
%defattr(-,root,root)
%{_rpmmacrodir}/macros.rails
/usr/lib/rpm/fileattrs/gemfile.attr
/usr/lib/rpm/gemfile.rb

%changelog
