#
# spec file for package kubernetes-dashboard
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


Name:           kubernetes-dashboard
Version:        27408f19
Release:        0
Summary:        General-purpose web UI for Kubernetes clusters
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            https://github.com/kubernetes/dashboard
Source:         %{name}-%{version}.tar.xz
Source1:        node_modules.tar.xz
Patch0:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go >= 1.8
BuildRequires:  golang-packaging
BuildRequires:  gyp
BuildRequires:  java-openjdk
BuildRequires:  nodejs8
BuildRequires:  nodejs8-devel
BuildRequires:  npm8
BuildRequires:  xz
# Extracted from `npm list --depth 0 --json`
Provides:       bundled(js(ace-builds)) = 1.2.9
Provides:       bundled(js(angular)) = 1.6.6
Provides:       bundled(js(angular-animate)) = 1.6.6
Provides:       bundled(js(angular-aria)) = 1.6.6
Provides:       bundled(js(angular-clipboard)) = 1.6.2
Provides:       bundled(js(angular-cookies)) = 1.6.6
Provides:       bundled(js(angular-file-saver)) = 1.1.3
Provides:       bundled(js(angular-material)) = 1.1.5
Provides:       bundled(js(angular-messages)) = 1.6.6
Provides:       bundled(js(angular-mocks)) = 1.6.6
Provides:       bundled(js(angular-resource)) = 1.6.6
Provides:       bundled(js(angular-sanitize)) = 1.6.6
Provides:       bundled(js(angular-ui-ace)) = 0.2.3
Provides:       bundled(js(angular-utils-pagination)) = 0.11.1
Provides:       bundled(js(ansi_up)) = 2.0.2
Provides:       bundled(js(async)) = 2.6.0
Provides:       bundled(js(babel)) = 6.23.0
Provides:       bundled(js(babel-core)) = 6.26.0
Provides:       bundled(js(babel-loader)) = 7.1.2
Provides:       bundled(js(babel-plugin-istanbul)) = 4.1.5
Provides:       bundled(js(babel-preset-env)) = 1.6.1
Provides:       bundled(js(babelify)) = 8.0.0
Provides:       bundled(js(browser-sync)) = 2.23.5
Provides:       bundled(js(browser-sync-spa)) = 1.0.3
Provides:       bundled(js(browserify)) = undefined
Provides:       bundled(js(clang-format)) = 1.1.0
Provides:       bundled(js(d3)) = 3.5.17
Provides:       bundled(js(del)) = 3.0.0
Provides:       bundled(js(eslint-plugin-angular)) = 3.1.1
Provides:       bundled(js(file-exists)) = 5.0.1
Provides:       bundled(js(google-closure-compiler)) = 20171203.0.0
Provides:       bundled(js(google-closure-library)) = 20171203.0.0
Provides:       bundled(js(gulp)) = 3.9.1
Provides:       bundled(js(gulp-autoprefixer)) = 4.1.0
Provides:       bundled(js(gulp-browserify)) = 0.5.1
Provides:       bundled(js(gulp-cheerio)) = 0.6.2
Provides:       bundled(js(gulp-clang-format)) = 1.0.23
Provides:       bundled(js(gulp-codecov.io)) = 1.0.1
Provides:       bundled(js(gulp-concat)) = 2.6.1
Provides:       bundled(js(gulp-css-url-adjuster)) = 0.2.3
Provides:       bundled(js(gulp-eslint)) = 4.0.0
Provides:       bundled(js(gulp-filter)) = 5.0.1
Provides:       bundled(js(gulp-findreplace)) = 1.5.0
Provides:       bundled(js(gulp-flatten)) = 0.4.0
Provides:       bundled(js(gulp-header-license)) = 1.0.9
Provides:       bundled(js(gulp-htmlmin)) = 4.0.0
Provides:       bundled(js(gulp-if)) = 2.0.2
Provides:       bundled(js(gulp-inject)) = 4.3.0
Provides:       bundled(js(gulp-license-check)) = 1.2.1
Provides:       bundled(js(gulp-minify-css)) = 1.2.4
Provides:       bundled(js(gulp-modify)) = 0.1.1
Provides:       bundled(js(gulp-protractor)) = 4.1.0
Provides:       bundled(js(gulp-rename)) = 1.2.2
Provides:       bundled(js(gulp-replace)) = 0.6.1
Provides:       bundled(js(gulp-replace-task)) = 0.11.0
Provides:       bundled(js(gulp-rev-all)) = 0.9.7
Provides:       bundled(js(gulp-sass)) = 3.1.0
Provides:       bundled(js(gulp-sass-lint)) = 1.3.4
Provides:       bundled(js(gulp-size)) = 3.0.0
Provides:       bundled(js(gulp-sourcemaps)) = 2.6.1
Provides:       bundled(js(gulp-uglify)) = 3.0.0
Provides:       bundled(js(gulp-useref)) = 3.1.3
Provides:       bundled(js(gulp-util)) = 3.0.8
Provides:       bundled(js(gulp-watch)) = 5.0.0
Provides:       bundled(js(gulp-xslt)) = 3.0.0
Provides:       bundled(js(hterm)) = 1.0.0
Provides:       bundled(js(html-minifier)) = 3.5.6
Provides:       bundled(js(http-proxy-middleware)) = 0.17.4
Provides:       bundled(js(js-beautify)) = 1.7.4
Provides:       bundled(js(jsesc)) = 2.5.1
Provides:       bundled(js(karma)) = 2.0.0
Provides:       bundled(js(karma-browserify)) = 5.1.2
Provides:       bundled(js(karma-chrome-launcher)) = 2.2.0
Provides:       bundled(js(karma-closure)) = 0.1.1
Provides:       bundled(js(karma-coverage)) = 1.1.1
Provides:       bundled(js(karma-jasmine)) = 1.1.0
Provides:       bundled(js(karma-jasmine-jquery)) = 0.1.1
Provides:       bundled(js(karma-ng-html2js-preprocessor)) = 1.0.0
Provides:       bundled(js(karma-sauce-launcher)) = 1.1.0
Provides:       bundled(js(karma-sourcemap-loader)) = 0.3.7
Provides:       bundled(js(lodash)) = 4.17.4
Provides:       bundled(js(material-design-icons)) = 3.0.1
Provides:       bundled(js(merge-stream)) = 1.0.1
Provides:       bundled(js(napa)) = 3.0.0
Provides:       bundled(js(npm-check-updates)) = 2.14.0
Provides:       bundled(js(nvd3)) = 1.8.6
Provides:       bundled(js(proxy-middleware)) = 0.15.0
Provides:       bundled(js(q)) = 1.5.1
Provides:       bundled(js(regexp-clone)) = 0.0.1
Provides:       bundled(js(roboto-fontface)) = 0.8.0
Provides:       bundled(js(semver)) = 5.4.1
Provides:       bundled(js(sockjs-client)) = 1.1.4
Provides:       bundled(js(through2)) = 2.0.3
Provides:       bundled(js(uglify-save-license)) = 0.4.1
Provides:       bundled(js(uirouter/angularjs)) = 1.0.10
Provides:       bundled(js(uirouter/core)) = 5.0.11
Provides:       bundled(js(vinyl-paths)) = 2.1.0
Provides:       bundled(js(watchify)) = 3.9.0
Provides:       bundled(js(webpack-stream)) = 4.0.0
Provides:       bundled(js(wiredep)) = 4.0.0
Provides:       bundled(js(wrench)) = 1.5.9
# For now node_modules.tar.xz provides only x86_64 compatibles files
ExclusiveArch:  x86_64
%{go_nostrip}
%{go_provides}

%description
Kubernetes Dashboard is a general purpose, web-based UI for Kubernetes clusters. It allows users to manage applications running in the cluster and troubleshoot them, as well as manage the cluster itself.

%prep
tar -C %{_builddir} -xf %{SOURCE0}
tar -C %{_builddir} -xf %{SOURCE1}
%autopatch -p1

%build
mkdir -p ~/.node-gyp/8.11.4/include && ln -sf %{_includedir}/node8 ~/.node-gyp/8.11.4/include/node

nodegyp=`pwd`/node_modules/node-gyp/bin/node-gyp.js
# dirs have been prepared online with node-gyp configure
for dir in node_modules/libxmljs-mt node_modules/gulp-xslt/node_modules/libxslt node_modules/node-sass ; do
#   (cd $dir && $nodegyp build)
    make -C $dir/build %{?_smp_mflags}
done
cp -l node_modules/node-sass/{build/Release/binding.node,vendor/linux-x64-57/}
# taskset required to avoid race from parallelism https://github.com/kubernetes/dashboard/issues/3234
taskset 1 node node_modules/gulp/bin/gulp.js build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard
install -m755 dist/amd64/dashboard %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard
install -m644 dist/amd64/locale_conf.json %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard
cp -r dist/amd64/public %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard
cp README.md %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard/
cp LICENSE %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard/
%fdupes -s %{buildroot}%{_localstatedir}/lib/kubernetes-dashboard/public
ln -s %{_localstatedir}/lib/kubernetes-dashboard/dashboard %{buildroot}%{_bindir}/kubernetes-dashboard

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_localstatedir}/lib/kubernetes-dashboard/
%{_localstatedir}/lib/kubernetes-dashboard/public/
%{_localstatedir}/lib/kubernetes-dashboard/dashboard
%{_localstatedir}/lib/kubernetes-dashboard/locale_conf.json
%{_bindir}/kubernetes-dashboard

%changelog
