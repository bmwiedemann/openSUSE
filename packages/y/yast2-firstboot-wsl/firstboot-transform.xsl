<!-- awesome xslt by Fabian -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:y="http://www.suse.com/1.0/yast2ns" xmlns="http://www.suse.com/1.0/yast2ns" xmlns:config="http://www.suse.com/1.0/configns">
  <xsl:output indent="yes"/>

  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="y:module[y:name = 'registration']/y:enabled/text()">
    <xsl:text>true</xsl:text>
  </xsl:template>
</xsl:stylesheet>
