package main;

import app.StartDesktopApp;
import utils.CliWrapper;
import utils.HyperAgentFactory;

public class LaunchLudii {

    public static void main(String args[]) {

	HyperAgentFactory.registerHyperAgents();

	if (args.length > 0) {
	    CliWrapper.runCommand(args);
	} else {
	    StartDesktopApp.main(args);
	}
    }
}
