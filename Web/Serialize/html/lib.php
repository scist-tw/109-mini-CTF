<?php

class User {
    private $name;
    function __construct($username) {
        $this->name = $username;
    }
    function __toString() {
        return htmlentities($this->name);
    }
    # Fast Destruct
    function __destruct() {
        echo "You found backdoor!!!" . PHP_EOL;
        echo shell_exec("echo Hello, hacker $this->name");
    }
    function isadmin() {
        return $this->name == 'admin';
    }
}
