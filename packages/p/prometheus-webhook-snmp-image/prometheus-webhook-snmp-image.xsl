<?xml version="1.0"
      encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml"
              encoding="UTF-8"
              indent="yes"/>
  <xsl:template match="/">
    <xsl:comment> OBS-ExclusiveArch: aarch64 x86_64 </xsl:comment>
    <xsl:comment>
      This file is generated, don't manually modify this file.
    </xsl:comment>

    <image xmlns:suse_label_helper="com.suse.label_helper"
           schemaversion="6.9"
           name="prometheus-webhook-snmp-image">

      <description type="system">
        <author>SUSE LLC</author>
        <contact>https://bugs.opensuse.org</contact>
        <specification>Image containing Prometheus Alertmanager receiver for SNMP traps</specification>
      </description>

      <preferences>
        <type image="docker">
          <xsl:attribute name="derived_from">
            <xsl:value-of select="param/image"/>
          </xsl:attribute>

          <containerconfig tag="latest"
                           maintainer="SUSE LLC (https://bugs.opensuse.org)">
            <xsl:attribute name="additionaltags">
              <xsl:value-of select="param/tags"/>,%PKG_VERSION%,%PKG_VERSION%.%RELEASE%</xsl:attribute>
            <xsl:attribute name="name">
              <xsl:value-of select="param/name"/>
            </xsl:attribute>

            <environment>
              <env name="PATH" value="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"/>
              <env name="ARGS" value="--debug"/>
              <env name="RUN_ARGS" value=""/>
            </environment>

            <subcommand execute="/bin/sh">
              <argument name="-c"/>
              <argument name="exec /usr/bin/prometheus-webhook-snmp $ARGS run $RUN_ARGS"/>
            </subcommand>

            <labels>
              <suse_label_helper:add_prefix>
                <xsl:attribute name="prefix">
                  <xsl:value-of select="param/prefix"/>
                </xsl:attribute>

                <label name="org.opencontainers.image.title"
                       value="Prometheus Alertmanager SNMP webhook"/>
                <label name="org.opencontainers.image.description"
                       value="Image containing Prometheus Alertmanager receiver for SNMP traps"/>
                <label name="org.opencontainers.image.version"
                       value="v%PKG_VERSION%.%RELEASE%"/>
                <label name="org.opencontainers.image.created"
                       value="%BUILDTIME%"/>
                <label name="org.opencontainers.image.vendor"
                       value="SUSE LLC"/>

                <label name="org.opencontainers.image.url">
                  <xsl:attribute name="value">
                    <xsl:value-of select="param/url"/>
                  </xsl:attribute>
                </label>
                <label name="org.opensuse.reference">
                  <xsl:attribute name="value">
                    <xsl:value-of select="param/reference"/>
                  </xsl:attribute>
                </label>

                <label name="org.openbuildservice.disturl"
                       value="%DISTURL%"/>
              </suse_label_helper:add_prefix>

              <xsl:for-each select="param/labels/label">
                <label>
                  <xsl:attribute name="name">
                    <xsl:value-of select="name"/>
                  </xsl:attribute>
                  <xsl:attribute name="value">
                    <xsl:value-of select="value"/>
                  </xsl:attribute>
                </label>
              </xsl:for-each>
            </labels>
            <history author="SUSE LLC">Install Prometheus Alertmanager receiver for SNMP traps</history>
          </containerconfig>
        </type>

        <version>1.0.0</version>
        <packagemanager>zypper</packagemanager>
        <rpm-check-signatures>false</rpm-check-signatures>
        <rpm-excludedocs>true</rpm-excludedocs>
        <locale>en_US</locale>
        <keytable>us.map.gz</keytable>
      </preferences>

      <packages type="bootstrap">
        <package name="prometheus-webhook-snmp"/>
        <package name="python3-prometheus_client"/>
      </packages>

      <repository type='rpm-md'>
        <source path='obsrepositories:/'/>
      </repository>
    </image>
  </xsl:template>
</xsl:stylesheet>
