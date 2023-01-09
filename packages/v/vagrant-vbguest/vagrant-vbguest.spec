#
# spec file for package vagrant-vbguest
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


%define mod_name vagrant-vbguest
%define mod_full_name %{mod_name}-%{version}
Name:           vagrant-vbguest
Version:        0.31.0
Release:        0
Summary:        Vagrant provider for vbguest
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/dotless-de/vagrant-vbguest
Source0:        https://rubygems.org/gems/%{mod_full_name}.gem
# Prevent have choice for rubygem(ruby:2.6.0:builder) >= 2.1.2
BuildRequires:  %{rubygem builder >= 3.2 }
# Prevent have choice for rubygem(ruby:2.6.0:ffi) >= 0.5.0
BuildRequires:  %{rubygem ffi >= 1.10 }
# Prevent have choice for rubygem(ruby:2.6.0:mime-types) >= 2
BuildRequires:  %{rubygem mime-types >= 3 }
BuildRequires:  %{ruby} >= 2.5
BuildRequires:  ruby-macros >= 5
BuildRequires:  vagrant
#  s.add_dependency "i18n"
Requires:       %{rubygem i18n}
#  s.add_dependency "log4r"
Requires:       %{rubygem log4r}
#  s.add_dependency "micromachine", "~> 3.0"
Requires:       %{rubygem micromachine:3}
Requires:       vagrant
Requires:       virtualbox
ExclusiveArch:  x86_64

%description
This is a Vagrant plugin that adds an Libvirt provider to Vagrant, allowing
Vagrant to control and provision machines via Libvirt toolkit.

%package        doc
Summary:        Documentation for vagrant-vbguest
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
This package contains the documentation for the vagrant-vbguest plugin.

%global vagrant_plugin_name %{name}

%prep
%gem_unpack

%build
%{gem_build}

%install
%vagrant_plugin_install

%check

%files
%{vagrant_plugin_instdir}
%{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%doc %{vagrant_plugin_instdir}/Readme.md
%license %{vagrant_plugin_instdir}/LICENSE

%exclude %{vagrant_plugin_instdir}/.*
%exclude %{vagrant_plugin_instdir}/Gemfile
%exclude %{vagrant_plugin_instdir}/Rakefile
%exclude %{vagrant_plugin_instdir}/README.md
%exclude %{vagrant_plugin_instdir}/LICENSE

%files doc
%doc %{vagrant_plugin_docdir}

%changelog
