<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:suse_label_helper="com.suse.label_helper">
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="suse_label_helper:add_prefix">
    <xsl:apply-templates select="label"/>
    <xsl:apply-templates select="label" mode="add_prefix"/>
  </xsl:template>

  <xsl:template match="label" mode="add_prefix">
    <label>
      <xsl:attribute name="name">
        <xsl:value-of select="../@prefix" />
        <xsl:text>.</xsl:text>
        <xsl:call-template name="last-domain-part">
          <xsl:with-param name="string" select="@name" />
        </xsl:call-template>
      </xsl:attribute>
      <xsl:attribute name="value">
        <xsl:value-of select="@value" />
      </xsl:attribute>
    </label>
  </xsl:template>

  <xsl:template name="last-domain-part">
  <xsl:param name="string" />
  <xsl:choose>
    <xsl:when test="contains($string, '.')">
      <xsl:call-template name="last-domain-part">
        <xsl:with-param name="string"
          select="substring-after($string, '.')" />
      </xsl:call-template>
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="$string" />
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>
</xsl:stylesheet>
