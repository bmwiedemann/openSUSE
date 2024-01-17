package org.fedoraproject;

import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugin.AbstractMojo;

/**
 * Empty goal to fix
 * @goal empty
 * @phase clean
 */
public class EmptyMojo
    extends AbstractMojo
{
    public void execute()
        throws MojoExecutionException, MojoFailureException
    {
    }
}
