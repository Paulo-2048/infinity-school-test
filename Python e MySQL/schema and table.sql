-- -----------------------------------------------------
-- Schema ig_store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ig_store` DEFAULT CHARACTER SET utf8 ;
USE `ig_store` ;

-- -----------------------------------------------------
-- Table `ig_store`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ig_store`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(145) NOT NULL,
  `email` VARCHAR(145) NOT NULL,
  `password` VARCHAR(145) NOT NULL,
  `date` DATETIME NOT NULL,
  `acess` INT NOT NULL DEFAULT '1',
  PRIMARY KEY (`iduser`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb3;