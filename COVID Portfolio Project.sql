use portfoliodb;

select * from coviddeaths
order by 3, 4;

select * from covidvaccinations;

select location, date, total_cases, new_cases, total_deaths, population 
from coviddeaths order by 1, 2;

-- Looking at Total Cases vs Total Deaths
-- shows likelihood of dying if you contract covid in your country

select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_Percentage
from coviddeaths 
where location like '%india%'
order by 1, 2;

-- Looking at Total Cases vs Populations
-- Shows what percentage of population got Covid

select location, date, total_cases, population, (total_cases/population)*100 as PercentagePolulationInfected
from coviddeaths 
-- where location like '%india%'
order by 1, 2;

-- Looking at countries with highest infection rate compared to population

select location, population,MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentagePolulationInfected
from coviddeaths 
Group By location, population
order by PercentagePolulationInfected desc;

-- Showing Countries with Highest Death Count per Polulation

select location, Max(total_deaths) as TotalDeathCount
from coviddeaths 
Group By location
order by TotalDeathCount desc;

-- Let's break down things down by continents

select continent, Max(total_deaths) as TotalDeathCount
from coviddeaths 
where continent is not null
Group By continent
order by TotalDeathCount desc; 

-- Showing the continent with the highest death count per population

select continent, Max(total_deaths) as TotalDeathCount
from coviddeaths 
where continent is not null
Group By continent
order by TotalDeathCount desc; 

-- Global Numbers

select date, sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, sum(new_deaths)/sum(new_cases)*100 as Death_Percentage
from coviddeaths 
where continent is not null
group by date
order by Death_Percentage desc;

-- Looking at Total Population Vaccinations

select d.continent, d.location, d.date, population, v.new_vaccinations
, sum(v.new_vaccinations) over (partition by d.location order by d.location, d.date) as RollingPeopleVaccinations
-- , (RollingPeopleVaccinations/population)*100
from coviddeaths d join covidvaccinations v
on d.location = v.location and d.date = v.date
where d.continent is not null
order by 2, 3;

with popvsVac(Continent, location, date, population, new_vaccinations, RollingPeopleaccinations) as (
select d.continent, d.location, d.date, population, v.new_vaccinations
, sum(v.new_vaccinations) over (partition by d.location order by d.location, d.date) as RollingPeopleVaccinations
from coviddeaths d join covidvaccinations v
on d.location = v.location and d.date = v.date
where d.continent is not null
)
select * from popvsVac;



-- Temp Table

drop table if exists #PercentPopulation
create Table #PercentPopulation
(
Continent nvarchar(255), location nvarchar(255), 
Date datetime, population numeric, New_vaccinations numeric, RollingPeopleVaccinations numeric);
 
 
insert into #PercentPopulation
select d.continent, d.location, d.date, population, v.new_vaccinations
, sum(v.new_vaccinations) over (partition by d.location order by d.location, d.date) as RollingPeopleVaccinations
-- , (RollingPeopleVaccinations/population)*100
from coviddeaths d join covidvaccinations v
on d.location = v.location and d.date = v.date
where d.continent is not null
order by 2, 3;

select * from #PercentPopulation;

