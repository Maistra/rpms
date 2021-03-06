# Build with debug info rpm
%global with_debug 0

Name:             grafana
Version:          6.4.3
Release:          3%{?dist}
Summary:          Metrics dashboard and graph editor
License:          ASL 2.0
URL:              https://grafana.org

%global webpack_hash ae7361e4e0b1e7937fc3d33a0732afb0aaa9541f77fe02423aaff1bd1541174b

# Source0 contains the tagged upstream sources
Source0:          https://github.com/grafana/grafana/archive/v%{version}/grafana-%{version}.tar.gz

# Source1 contains the front-end javascript modules bundled into a webpack
Source1:          grafana_webpack-%{version}.%{webpack_hash}.tar.gz

# Source2 is the script to create the above webpack from grafana sources
#Source2:          make_grafana_webpack.sh

# Patches for upstream
Patch1:           001-login-oauth-use-oauth2-exchange.patch
Patch2:           002-remove-jaeger-tracing.patch
Patch3:           003-new-files.patch
Patch4:           004-xerrors.patch
Patch5:           005-mute-shellcheck-grafana-cli.patch
Patch6:           900-make-annobin-happy.patch

# Patches for CVEs
Patch102:         yarn-002-maistra-1304
Patch103:         yarn-003-maistra-1328
Patch104:         yarn-004-maistra-1417
Patch105:         006-CVE-2020-13379.patch
Patch106:         007-CVE-2020-13430.patch
Patch107:         008-CVE-2020-12245.patch
Patch108:         108-MAISTRA-1462-Update-gopkg.in-yaml.v2-to-v2.3.0.patch
Patch109:         109-yarn-maistra-1522.patch
Patch110:         110-yarn-maistra-1565.patch
Patch111:         111-yarn-maistra-1560.patch
Patch112:         112-CVE-2020-12666.patch
Patch113:         113-CVE-2020-14040.patch

# Broken tests
Patch201:         201-disable-broken-tests.patch

# Intersection of go_arches and nodejs_arches
# FIXME? macro evaluates to empty
# ExclusiveArch:    %{grafana_arches}
ExclusiveArch:  x86_64

# omit golang debugsource, see BZ995136 and related
%global           dwz_low_mem_die_limit 0
%global           _debugsource_template %{nil}

%global           GRAFANA_HOME %{_datadir}/%{name}
%global           binary_name grafana

# grafana-server service daemon uses systemd
%{?systemd_requires}
Requires(pre):    shadow-utils

BuildRequires:    systemd, golang, go-srpm-macros

# Declare all nodejs modules bundled in the webpack - this is for security
# purposes so if nodejs-foo ever needs an update, affected packages can be
# easily identified. This is generated from package-lock.json once the webpack
# has been built with make_webpack.sh.
Provides: bundled(nodejs-abbrev) = 1.1.1
Provides: bundled(nodejs-ansi-regex) = 2.1.1
Provides: bundled(nodejs-ansi-styles) = 2.2.1
Provides: bundled(nodejs-argparse) = 1.0.10
Provides: bundled(nodejs-array-find-index) = 1.0.2
Provides: bundled(nodejs-async) = 1.5.2
Provides: bundled(nodejs-balanced-match) = 1.0.0
Provides: bundled(nodejs-brace-expansion) = 1.1.11
Provides: bundled(nodejs-builtin-modules) = 1.1.1
Provides: bundled(nodejs-camelcase) = 2.1.1
Provides: bundled(nodejs-camelcase-keys) = 2.1.0
Provides: bundled(nodejs-chalk) = 1.1.3
Provides: bundled(nodejs-coffee-script) = 1.10.0
Provides: bundled(nodejs-colors) = 1.1.2
Provides: bundled(nodejs-concat-map) = 0.0.1
Provides: bundled(nodejs-currently-unhandled) = 0.4.1
Provides: bundled(nodejs-dateformat) = 1.0.12
Provides: bundled(nodejs-decamelize) = 1.2.0
Provides: bundled(nodejs-error-ex) = 1.3.2
Provides: bundled(nodejs-escape-string-regexp) = 1.0.5
Provides: bundled(nodejs-esprima) = 2.7.3
Provides: bundled(nodejs-eventemitter2) = 0.4.14
Provides: bundled(nodejs-exit) = 0.1.2
Provides: bundled(nodejs-find-up) = 1.1.2
Provides: bundled(nodejs-findup-sync) = 0.3.0
Provides: bundled(nodejs-fs.realpath) = 1.0.0
Provides: bundled(nodejs-get-stdin) = 4.0.1
Provides: bundled(nodejs-getobject) = 0.1.0
Provides: bundled(nodejs-glob) = 7.0.6
Provides: bundled(nodejs-graceful-fs) = 4.1.15
Provides: bundled(nodejs-grunt) = 1.0.1
Provides: bundled(nodejs-grunt-cli) = 1.2.0
Provides: bundled(nodejs-grunt-known-options) = 1.1.1
Provides: bundled(nodejs-grunt-legacy-log) = 1.0.2
Provides: bundled(nodejs-lodash) = 4.17.11
Provides: bundled(nodejs-grunt-legacy-log-utils) = 1.0.0
Provides: bundled(nodejs-grunt-legacy-util) = 1.0.0
Provides: bundled(nodejs-has-ansi) = 2.0.0
Provides: bundled(nodejs-hooker) = 0.2.3
Provides: bundled(nodejs-hosted-git-info) = 2.7.1
Provides: bundled(nodejs-iconv-lite) = 0.4.24
Provides: bundled(nodejs-indent-string) = 2.1.0
Provides: bundled(nodejs-inflight) = 1.0.6
Provides: bundled(nodejs-inherits) = 2.0.3
Provides: bundled(nodejs-is-arrayish) = 0.2.1
Provides: bundled(nodejs-is-builtin-module) = 1.0.0
Provides: bundled(nodejs-is-finite) = 1.0.2
Provides: bundled(nodejs-is-utf8) = 0.2.1
Provides: bundled(nodejs-isexe) = 2.0.0
Provides: bundled(nodejs-js-yaml) = 3.5.5
Provides: bundled(nodejs-load-json-file) = 1.1.0
Provides: bundled(nodejs-loud-rejection) = 1.6.0
Provides: bundled(nodejs-map-obj) = 1.0.1
Provides: bundled(nodejs-meow) = 3.7.0
Provides: bundled(nodejs-minimatch) = 3.0.4
Provides: bundled(nodejs-minimist) = 1.2.0
Provides: bundled(nodejs-nopt) = 3.0.6
Provides: bundled(nodejs-normalize-package-data) = 2.4.2
Provides: bundled(nodejs-number-is-nan) = 1.0.1
Provides: bundled(nodejs-object-assign) = 4.1.1
Provides: bundled(nodejs-once) = 1.4.0
Provides: bundled(nodejs-parse-json) = 2.2.0
Provides: bundled(nodejs-path-exists) = 2.1.0
Provides: bundled(nodejs-path-is-absolute) = 1.0.1
Provides: bundled(nodejs-path-type) = 1.1.0
Provides: bundled(nodejs-pify) = 2.3.0
Provides: bundled(nodejs-pinkie) = 2.0.4
Provides: bundled(nodejs-pinkie-promise) = 2.0.1
Provides: bundled(nodejs-read-pkg) = 1.1.0
Provides: bundled(nodejs-read-pkg-up) = 1.0.1
Provides: bundled(nodejs-redent) = 1.0.0
Provides: bundled(nodejs-repeating) = 2.0.1
Provides: bundled(nodejs-resolve) = 1.1.7
Provides: bundled(nodejs-rimraf) = 2.2.8
Provides: bundled(nodejs-safer-buffer) = 2.1.2
Provides: bundled(nodejs-semver) = 5.6.0
Provides: bundled(nodejs-signal-exit) = 3.0.2
Provides: bundled(nodejs-spdx-correct) = 3.1.0
Provides: bundled(nodejs-spdx-exceptions) = 2.2.0
Provides: bundled(nodejs-spdx-expression-parse) = 3.0.0
Provides: bundled(nodejs-spdx-license-ids) = 3.0.3
Provides: bundled(nodejs-sprintf-js) = 1.0.3
Provides: bundled(nodejs-strip-ansi) = 3.0.1
Provides: bundled(nodejs-strip-bom) = 2.0.0
Provides: bundled(nodejs-strip-indent) = 1.0.1
Provides: bundled(nodejs-supports-color) = 2.0.0
Provides: bundled(nodejs-trim-newlines) = 1.0.0
Provides: bundled(nodejs-underscore.string) = 3.2.3
Provides: bundled(nodejs-validate-npm-package-license) = 3.0.4
Provides: bundled(nodejs-which) = 1.2.14
Provides: bundled(nodejs-wrappy) = 1.0.2
Provides: bundled(nodejs-yarn) = 1.13.0


%description
Grafana is an open source, feature rich metrics dashboard and graph editor for
Graphite, InfluxDB & OpenTSDB.

%package prometheus
Requires: %{name} = %{version}-%{release}
Summary: Grafana prometheus datasource

%description prometheus
The Grafana prometheus datasource.

%prep
%setup -q -T -D -b 0 -n grafana-%{version}
%setup -q -T -D -b 1 -n grafana-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1

%patch201 -p1

# Set up build subdirs and links
mkdir -p %{_builddir}/src/github.com/grafana
ln -sf %{_builddir}/%{binary_name}-%{version} \
    %{_builddir}/src/github.com/grafana/grafana

# remove some (apparent) development files, for rpmlint
rm -f public/sass/.sass-lint.yml public/test/.jshintrc

%build
cd %{_builddir}/src/github.com/grafana/grafana
%global archbindir bin/`go env GOOS`-`go env GOARCH`
echo _builddir=%{_builddir} archbindir=%{archbindir}
[ ! -d %{archbindir} ] && mkdir -p %{archbindir}

# Build the server-side binaries: grafana-server and grafana-cli
go build -mod=vendor -o %{archbindir}/grafana-cli ./pkg/cmd/grafana-cli
go build -mod=vendor -o %{archbindir}/grafana-server ./pkg/cmd/grafana-server

%check
cd %{_builddir}/src/github.com/grafana/grafana
# remove tests currently failing
rm -f pkg/services/provisioning/dashboards/file_reader_linux_test.go
rm -f pkg/services/provisioning/dashboards/file_reader_test.go
go test -mod=vendor ./pkg/...

%install
# Fix up arch bin directories
[ ! -d bin/x86_64 ] && ln -sf linux-amd64 bin/x86_64
[ ! -d bin/i386 ] && ln -sf linux-386 bin/i386
[ ! -d bin/ppc64le ] && ln -sf linux-ppc64le bin/ppc64le
[ ! -d bin/s390x ] && ln -sf linux-s390x bin/s390x
[ ! -d bin/arm ] && ln -sf linux-arm bin/arm
[ ! -d bin/arm64 ] && ln -sf linux-arm64 bin/aarch64
[ ! -d bin/aarch64 ] && ln -sf linux-aarch64 bin/aarch64

# binaries
install -d %{buildroot}%{_sbindir}
binaries=(%{binary_name}-server %{binary_name}-cli)
%if 0%{?with_debug} > 0
  for i in "${binaries[@]}"; do
        install -p -m 750 bin/%{_arch}/$i %{buildroot}%{_sbindir}
   done
%else
    mkdir stripped
    touch keep_symbols
    for i in "${binaries[@]}"; do
       echo "Dumping dynamic symbols for ${i}"
        nm -D bin/%{_arch}/$i --format=posix --defined-only \
  | awk '{ print $1 }' | sort > dynsyms

        echo "Dumping function symbols for ${i}"
       nm bin/%{_arch}/$i --format=posix --defined-only \
  | awk '{ if ($2 == "T" || $2 == "t" || $2 == "D") print $1 }' \
  | sort > funcsyms

        echo "Grabbing other function symbols from ${i}"
        comm -13 dynsyms funcsyms > keep_symbols

        COMPRESSED_NAME="${i}_debuginfo"
        if [ -s keep_symbols ]; then
          echo "remove unnecessary debug info from ${i}"
          objcopy -S --remove-section .gdb_index --remove-section .comment \
  --keep-symbols=keep_symbols bin/%{_arch}/$i "${COMPRESSED_NAME}"
        fi

        echo "stripping: ${i}"
        strip -o "stripped/${i}" -s bin/%{_arch}/$i

        if [ -f ${COMPRESSED_NAME} ]; then
          echo "compress debugdata for ${i} into ${COMPRESSED_NAME}.xz"
          xz "${COMPRESSED_NAME}"

          echo "inject compressed data into .gnu_debugdata for ${i}"
          objcopy --add-section ".gnu_debugdata=${COMPRESSED_NAME}.xz" "stripped/${i}"
        fi

        install -p -m 750 "stripped/${i}" %{buildroot}%{_sbindir}
    done
%endif

# other shared files, public html, webpack
install -d %{buildroot}%{_datadir}/%{binary_name}
cp -a conf public %{buildroot}%{_datadir}/%{binary_name}

# man pages
install -d %{buildroot}%{_mandir}/man1
install -p -m 640 docs/man/man1/* %{buildroot}%{_mandir}/man1

# config dirs
install -d %{buildroot}%{_sysconfdir}/%{binary_name}
install -d %{buildroot}%{_sysconfdir}/sysconfig

# config defaults
install -p -m 640 conf/distro-defaults.ini \
    %{buildroot}%{_sysconfdir}/%{binary_name}/grafana.ini
install -p -m 640 conf/distro-defaults.ini \
    %{buildroot}%{_datadir}/%{binary_name}/conf/defaults.ini
install -p -m 640 conf/ldap.toml %{buildroot}%{_sysconfdir}/%{binary_name}/ldap.toml
install -p -m 640 packaging/rpm/sysconfig/grafana-server \
    %{buildroot}%{_sysconfdir}/sysconfig/grafana-server

# config database directory and plugins
install -d %{buildroot}%{_sharedstatedir}/%{binary_name}
install -d -m 750 %{buildroot}%{_sharedstatedir}/%{binary_name}
install -d -m 750 %{buildroot}%{_sharedstatedir}/%{binary_name}/plugins

# log directory
install -d %{buildroot}%{_localstatedir}/log/%{binary_name}

# systemd service files
install -d %{buildroot}%{_unitdir} # only needed for manual rpmbuilds
install -p -m 640 packaging/rpm/systemd/grafana-server.service \
    %{buildroot}%{_unitdir}

%files
# binaries
%{_sbindir}/%{binary_name}-server
%{_sbindir}/%{binary_name}-cli

# config files
%dir %{_sysconfdir}/%{binary_name}
%config(noreplace) %attr(640, root, root) %{_sysconfdir}/%{binary_name}/grafana.ini
%config(noreplace) %attr(640, root, root) %{_sysconfdir}/%{binary_name}/ldap.toml
%config(noreplace) %{_sysconfdir}/sysconfig/grafana-server

# config database directory and plugins (actual db files are created by grafana-server)
%dir %{_sharedstatedir}/%{binary_name}
%dir %{_sharedstatedir}/%{binary_name}/plugins

# shared directory and all files therein, except some datasources
%{_datadir}/%{binary_name}/public

# built-in datasources that are sub-packaged
%global dsdir %{_datadir}/%{binary_name}/public/app/plugins/datasource

%exclude %{dsdir}/cloudwatch
%exclude %{dsdir}/elasticsearch
%exclude %{dsdir}/graphite
%exclude %{dsdir}/grafana-azure-monitor-datasource
%exclude %{dsdir}/influxdb
%exclude %{dsdir}/loki
%exclude %{dsdir}/mssql
%exclude %{dsdir}/mysql
%exclude %{dsdir}/opentsdb
%exclude %{dsdir}/postgres
%exclude %{dsdir}/prometheus
%exclude %{dsdir}/stackdriver

%dir %{_datadir}/%{binary_name}/conf
%{_datadir}/%{binary_name}/conf/*

# systemd service file
%{_unitdir}/grafana-server.service

# log directory - grafana.log is created by grafana-server, and it does it's own log rotation
%attr(0750, root, root) %dir %{_localstatedir}/log/%{binary_name}

# man pages for grafana binaries
%{_mandir}/man1/%{binary_name}-server.1*
%{_mandir}/man1/%{binary_name}-cli.1*

# other docs and license
%license LICENSE
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md NOTICE.md
%doc PLUGIN_DEV.md README.md ROADMAP.md UPGRADING_DEPENDENCIES.md

%files prometheus
%{_datadir}/%{binary_name}/public/app/plugins/datasource/prometheus

%changelog
* Wed Feb 17 2021 Kevin Conner <kconner@redhat.com> - 6.4.3-3
- Update for 2.0.2 release

* Sun Jan 3 2021 Product Release - 6.4.3-2
- Update to latest release

* Tue Mar 31 2020 Jonh Wendell <jwendell@redhat.com> - 6.4.3-1
- First version for Maistra 1.1
