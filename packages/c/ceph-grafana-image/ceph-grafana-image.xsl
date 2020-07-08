<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <xsl:comment> OBS-ExclusiveArch: aarch64 x86_64 </xsl:comment>
    <xsl:comment>
		This file is generated,
		don't manually modify this file,
		please check README
    </xsl:comment>
    <image schemaversion="6.9" name="ceph-grafana-image" 
      xmlns:suse_label_helper="com.suse.label_helper">

      <description type="system">
        <author>SUSE LLC</author>
        <contact>https://bugs.opensuse.org</contact>
        <specification>Grafana container image for Ceph</specification>
      </description>

      <preferences>
        <type image="docker">
          <xsl:attribute name="derived_from">
            <xsl:value-of select="param/image" />
          </xsl:attribute>
          <containerconfig tag="latest" maintainer="SUSE LLC (https://bugs.opensuse.org)">
            <xsl:attribute name="additionaltags">
              <xsl:value-of select="param/tags" />,%PKG_VERSION%,%PKG_VERSION%.%RELEASE%</xsl:attribute>
            <xsl:attribute name="name">
              <xsl:value-of select="param/name" />
            </xsl:attribute>

            <expose>
              <port number="3000/tcp"/>
            </expose>

            <entrypoint execute="bash">
              <argument name="/usr/local/bin/entrypoint.sh"/>
            </entrypoint>
            <subcommand clear="true"/>

            <labels>

              <suse_label_helper:add_prefix>
                <xsl:attribute name="prefix">
                  <xsl:value-of select="param/prefix" />
                </xsl:attribute>

                <label name="org.opencontainers.image.title" value="Grafana for Ceph"/>
                <label name="org.opencontainers.image.description" value="Grafana container image for Ceph"/>
                <label name="org.opencontainers.image.version" value="%PKG_VERSION%.%RELEASE%"/>
                <label name="org.opencontainers.image.created" value="%BUILDTIME%"/>
                <label name="org.opencontainers.image.vendor" value="SUSE LLC"/>

                <label name="org.opencontainers.image.url">
                  <xsl:attribute name="value">
                    <xsl:value-of select="param/url" />
                  </xsl:attribute>
                </label>

                <label name="org.openbuildservice.disturl" value="%DISTURL%"/>

                <label name="org.opensuse.reference">
                  <xsl:attribute name="value">
                    <xsl:value-of select="param/reference" />
                  </xsl:attribute>
                </label>

              </suse_label_helper:add_prefix>

              <xsl:for-each select="param/labels/label">
                <label>
                  <xsl:attribute name="name">
                    <xsl:value-of select="name" />
                  </xsl:attribute>
                  <xsl:attribute name="value">
                    <xsl:value-of select="value" />
                  </xsl:attribute>
                </label>
              </xsl:for-each>

            </labels>

            <history author="SUSE LLC">Install grafana and ceph dashboards</history>
          </containerconfig>
        </type>
        <version>1.0.0</version>
        <packagemanager>zypper</packagemanager>
        <rpm-check-signatures>false</rpm-check-signatures>
        <rpm-excludedocs>true</rpm-excludedocs>
        <locale>en_US</locale>
        <keytable>us.map.gz</keytable>
      </preferences>

      <repository>
        <source path='obsrepositories:/'/>
      </repository>

      <packages type="bootstrap">
        <xsl:for-each select="param/bootstrap-packages/package">
          <package>
            <xsl:attribute name="name">
              <xsl:value-of select="@name"/>
            </xsl:attribute>
          </package>
        </xsl:for-each>
        <package name="grafana"/>
        <package name="grafana-piechart-panel"/>
        <package name="grafana-status-panel"/>
        <package name="ceph-grafana-dashboards"/>
      </packages>
    </image>

  </xsl:template>

</xsl:stylesheet>
