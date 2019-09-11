# spec file for package dice
#
# Copyright (c) 2014 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
Name:           dice
Version:        0.7.10
Release:        0
%define mod_name dice
%define mod_full_name %{mod_name}-%{version}
%define rb_build_versions %{rb_default_ruby}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ruby-devel
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rice}
BuildRequires:  %{rubygem bundler}
BuildRequires:  %{rubygem cheetah >= 0.4.0}
BuildRequires:  %{rubygem gli >= 2.11.0}
BuildRequires:  %{rubygem abstract_method >= 1.2.1}
BuildRequires:  %{rubygem json >= 1.8.0}
BuildRequires:  %{rubygem inifile >= 2.0.2}

# Disable autogenerating "Requires:" headers for bundled gems.
%define __requires_exclude ^rubygem
Requires:       ruby >= 2.0
Requires:       ruby-solv
Requires:       curl
Url:            http://www.suse.com
Source0:        %{mod_full_name}.gem
Source1:        %{mod_name}-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Light Weight Image Build System
License:        GPL-3.0
Group:          Development/Languages/Ruby

%description
Given there is the need to build a kiwi appliance for a customer,
one wants to keep track of the updates from the distribution and
software vendors according to the components used in the appliance.
This leads to a regular rebuild of that appliance which should be
automatically triggered whenever the repository which stores all
the software packages has changed. With Dice there is a tool which
automatically builds all appliances stored in a directory

%prep

%build

%install
# Install the Ruby source
%gem_install \
  --symlink-binaries \
  --doc-files="COPYING key" \
  -f

# Change to ruby gem dir
pushd %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}

# Build CPP extensions
( cd lib/semaphore && ruby ./extconf.rb && make && rm -f semaphore.o )

# Bundle dependencies
cat > Gemfile <<EOT
gem "cheetah", ">= 0.4.0"
gem "gli", ">= 2.11.0"
gem "abstract_method", ">= 1.2.1"
%if %suse_version <= 1310
gem "json", ">= 1.8.0"
%endif
gem "inifile", ">= 2.0.2"
EOT

mkdir -p vendor/cache
cp %{_libdir}/ruby/gems/%{rb_ver}/cache/*.gem vendor/cache

bundle install --standalone --local

rm -rf vendor .bundle Gemfile Gemfile.lock

# Delete devel source
( cd lib/semaphore && rm -f semaphore.cpp Makefile extconf.rb )

# Move bash completion
mkdir -p %{buildroot}/etc/bash_completion.d
mv completion/dice.sh %{buildroot}/etc/bash_completion.d

popd

# Adapt the binary
# Here we do a surgery on the binary to actually load the bundled gems.
# This is a hack, but it can't be done anywhere else because the binary
# is generated during gem install.
sed -i '/gem/i \
Gem.path.unshift("%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/bundle/ruby/%{rb_ver}")

' %{buildroot}/usr/bin/dice.ruby*-%{version}

# Convert duplicate files to symlinks
%fdupes -s %{buildroot}

%gem_packages
%config /etc/bash_completion.d/dice.sh

%changelog
