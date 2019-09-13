#
# spec file for package machinery
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           machinery
Version:        1.24.1
Release:        0
%define binary_name machinery
%define mod_name machinery-tool
%define mod_full_name %{mod_name}-%{version}
%define mod_branch -%{version}
%define mod_weight 1

# Bundle gems for SUSE Linux Enterprise only because there they are not available
# outside of the build repos
%if 0%{?is_opensuse}
%define bundlegems 0
%else
%define bundlegems 1
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Require on SLES12 our Go version with s390x support
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse} != 1
BuildRequires:  go-s390x
%else
BuildRequires:  go
%endif
BuildRequires:  fdupes
BuildRequires:  ruby-macros >= 5
%define rb_build_versions %{rb_default_ruby}
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem bundler}
BuildRequires:  %{rubygem gem2rpm}
%if 0%{?bundlegems}
BuildRequires:  %{rubygem abstract_method < 2}
BuildRequires:  %{rubygem abstract_method >= 1.2}
BuildRequires:  %{rubygem builder < 4}
BuildRequires:  %{rubygem builder >= 3.2}
BuildRequires:  %{rubygem cheetah < 1}
BuildRequires:  %{rubygem cheetah >= 0.4}
BuildRequires:  %{rubygem diffy < 4}
BuildRequires:  %{rubygem diffy >= 3.0}
BuildRequires:  %{rubygem gli < 3}
BuildRequires:  %{rubygem gli >= 2.11}
BuildRequires:  %{rubygem haml >= 4.0}
BuildRequires:  %{rubygem json-schema < 3}
BuildRequires:  %{rubygem json-schema >= 2.2}
BuildRequires:  %{rubygem kramdown >= 1.3}
BuildRequires:  %{rubygem mimemagic < 1}
BuildRequires:  %{rubygem mimemagic >= 0.3}
BuildRequires:  %{rubygem sinatra >= 1.4}
BuildRequires:  %{rubygem tilt < 3}
BuildRequires:  %{rubygem tilt >= 2.0}
%else
Requires:       %{rubygem abstract_method < 2}
Requires:       %{rubygem abstract_method >= 1.2}
Requires:       %{rubygem builder < 4}
Requires:       %{rubygem builder >= 3.2}
Requires:       %{rubygem cheetah < 1}
Requires:       %{rubygem cheetah >= 0.4}
Requires:       %{rubygem diffy < 4}
Requires:       %{rubygem diffy >= 3.0}
Requires:       %{rubygem gli < 3}
Requires:       %{rubygem gli >= 2.11}
Requires:       %{rubygem haml >= 4.0}
Requires:       %{rubygem json-schema < 3}
Requires:       %{rubygem json-schema >= 2.2}
Requires:       %{rubygem kramdown >= 1.3}
Requires:       %{rubygem mimemagic < 1}
Requires:       %{rubygem mimemagic >= 0.3}
Requires:       %{rubygem sinatra >= 1.4}
Requires:       %{rubygem tilt < 3}
Requires:       %{rubygem tilt >= 2.0}
%endif
# Disable autogenerating "Requires:" headers for bundled gems.
%define __requires_exclude ^rubygem
Requires:       ruby >= 2.0
Requires:       sudo
Requires:       which
Url:            http://suse.com
Source0:        http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        %{binary_name}-rpmlintrc
Summary:        Systems management toolkit
License:        GPL-3.0-only
Group:          Development/Languages/Ruby

%description
Machinery is a systems management toolkit for Linux. It supports configuration
discovery, system validation, and service migration. It's based on the idea of a
universal system description.

%package doc
Summary:        RDoc and RI documentation for Machinery
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description doc
RDoc and RI documentation for Machinery. Machinery is a systems management
toolkit for Linux.

%prep

%build

%install
# Install the gem itself

%gem_install -f

%if %{?bundlegems}
# Bundle dependencies

pushd %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}

cat > Gemfile <<EOT
gem "cheetah", "~> 0.4"
gem "abstract_method", "~> 1.2"
gem "builder", "~> 3.2"
gem "gli", "~> 2.11"
gem "json-schema", "~> 2.2"
gem "haml", ">= 4.0"
gem "kramdown", ">= 1.3"
gem "tilt", "~> 2.0"
gem "sinatra", ">= 1.4"
gem "mimemagic", "~> 0.3"
gem "diffy", "~> 3.0"
EOT

mkdir -p vendor/cache
cp %{_libdir}/ruby/gems/%{rb_ver}/cache/*.gem vendor/cache

bundle install --standalone --local

popd
%endif

# Adapt the binary

# Remove the ruby version suffix from the machinery executable
if [ ! -f "%{buildroot}%{_bindir}/%{binary_name}" ]; then
  mv "%{buildroot}%{_bindir}/%{binary_name}"* "%{buildroot}%{_bindir}/%{binary_name}"
fi

%if %{?bundlegems}
# Here we do a surgery on the binary to actually load the bundled gems. This is
# a hack, but it can't be done anywhere else because the binary is generated
# during gem install.
sed -i '/gem /i \
Gem.path.unshift("%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/bundle/ruby/%{rb_ver}")

' %{buildroot}%{_bindir}/%{binary_name}
%endif

# Clean up obsolete extension doc
rm -rf %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/doc/extensions

# Man page & additional files

mkdir -p %{buildroot}%{_mandir}/man1
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/man/generated/%{binary_name}.1.gz %{buildroot}%{_mandir}/man1/
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/COPYING
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/NEWS

# Convert duplicate files to symlinks
# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}/%{_prefix}

%files
%defattr(-,root,root,-)
%{_bindir}/%{binary_name}
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_full_name}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/

%{_libdir}/ruby/gems/%{rb_ver}/extensions/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_full_name}.gemspec
%{_mandir}/man1/*.1.gz
%if 0%{?suse_version} < 1500
%doc COPYING NEWS
%else
%license COPYING
%doc NEWS
%endif

%files doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_full_name}/

%changelog
