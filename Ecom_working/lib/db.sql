-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema models_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `models_schema` ;

-- -----------------------------------------------------
-- Schema models_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `models_schema` DEFAULT CHARACTER SET utf8 ;
USE `models_schema` ;

-- -----------------------------------------------------
-- Table `models_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `models_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `models_schema`.`models`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `models_schema`.`models` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `param1` VARCHAR(45) NULL DEFAULT NULL,
  `param2` VARCHAR(45) NULL DEFAULT NULL,
  `param3` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_models_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_models_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `models_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;