#
# spec file for package velum
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           velum

# When you release a new version, set Version and branch accordingly.
# For example:
# Version:      1.0.0
# %%define branch 1.0.0

Version:        4.0.0+dev+git_r940_e589023f00ba7897b32676d7be6938e270b4e7bb
Release:        0
%define branch master
Summary:        Dashboard for CaasP
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubic-project/velum
Source:         %{branch}.tar.gz
Source2:        velum-rpmlintrc

Patch0:         0_set_default_salt_events_alter_time_column_value.rpm.patch

Patch1:         1_nodev.gem.patch

%define velumdir /srv/velum

Requires:       ruby >= 2.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ruby-macros >= 5
Obsoletes:      velum < %{version}
# javascript engine to build assets
BuildRequires:  nodejs
BuildRequires:  velum-branding

%define rb_build_versions %{rb_default_ruby}
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem bundler} >= 1.3.0
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-common-rails

# fixed gem dependent build requires
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
# if openSUSE Tumbleweed or SLE_15
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150000
BuildRequires:  libmariadb-devel
Requires:       mariadb-client
%else
BuildRequires:  libmysqlclient-devel < 10.1
Requires:       libmysqlclient18 < 10.1
%endif
Recommends:     mariadb
BuildRequires:  libffi-devel

BuildRequires:  %{rubygem bcrypt:3.1 >= 3.1.7}
BuildRequires:  %{rubygem bootstrap-sass:3.3 >= 3.3.7}
BuildRequires:  %{rubygem devise >= 4.3}
BuildRequires:  %{rubygem devise_ldap_authenticatable:0 >= 0.8}
BuildRequires:  %{rubygem font-awesome-rails:4 >= 4.7}
BuildRequires:  %{rubygem gravatar_image_tag:1.2 >= 1.2.0}
BuildRequires:  %{rubygem jbuilder:2 >= 2.5}
BuildRequires:  %{rubygem jquery-rails:4 >= 4.3}
BuildRequires:  %{rubygem minitest:5 >= 5.10}
BuildRequires:  %{rubygem mysql2:0.4 >= 0.4.10}
BuildRequires:  %{rubygem net-ldap:0 >= 0.11}
BuildRequires:  %{rubygem openid_connect:1 >= 1.1}
BuildRequires:  %{rubygem puma:3 >= 3.11}
BuildRequires:  %{rubygem rails:4.2 >= 4.2.10}
BuildRequires:  %{rubygem rails_stdout_logging:0.0 >= 0.0.5}
BuildRequires:  %{rubygem rake:12 >= 12.2}
BuildRequires:  %{rubygem sass-rails:5 >= 5.0}
BuildRequires:  %{rubygem slim:3 >= 3.0}
BuildRequires:  %{rubygem uglifier:4 >= 4.1}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
velum is the dashboard for CaasP to manage and deploy kubernetes clusters on top of MicroOS

This package has been built with commit e589023f00ba7897b32676d7be6938e270b4e7bb from branch master on date Thu, 11 Oct 2018 05:49:36 +0000

%prep
%setup -q -n velum-%{branch}
%rails_save_gemfile

%patch0 -p1

%patch1 -p1

%build
%rails_regen_gemfile_lock

install -d vendor/cache
cp %{_libdir}/ruby/gems/%{rb_ver}/cache/*.gem vendor/cache

export NOKOGIRI_USE_SYSTEM_LIBRARIES=1

# deploy gems
bundle install --retry=3 --local --deployment --without development test

# copy over the images from velum-branding
cp -R %{_datadir}/velum/images/* app/assets/images/branding/

VELUM_SECRETS_DIR=%{buildroot}%{velumdir}/tmp RAILS_ENV=production INCLUDE_ASSETS_GROUP=yes bundle exec rake assets:precompile
# fix permissions of generated assets
# this is necessary to make them linkable by fdupes later
for ext in woff woff2 eot ttf svg; do
  find . -name "*.$ext" -exec chmod -R 755 {} \;
done

# deploy gems without assets
bundle install --retry=3 --local --deployment --without development test assets

# clean unused gems
bundle clean

# install bundler
gem install --no-rdoc --no-ri --install-dir vendor/bundle/ruby/%{rb_ver}/ vendor/cache/bundler-*.gem

rm -rf vendor/cache

%install
install -d %{buildroot}%{velumdir}

cp -a . %{buildroot}%{velumdir}

for folder in log tmp; do
  rm -rf %{buildroot}%{velumdir}/$folder
  mkdir %{buildroot}%{velumdir}/$folder
done

%if 0%{?suse_version} >= 1500
  rm %{buildroot}%{velumdir}/LICENSE
%endif

%fdupes -s %{buildroot}/%{velumdir}

%files
%defattr(-,root,root)
%{velumdir}
%exclude %{velumdir}/spec
%doc %{velumdir}/README.md

%if 0%{?suse_version} < 1500
%doc %{velumdir}/LICENSE
%else
%license LICENSE
%endif

%changelog
