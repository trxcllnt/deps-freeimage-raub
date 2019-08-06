'use strict';

const { expect } = require('chai');
const { stub, spy } = require('sinon');

const deps = require('deps-freeimage-raub');


describe('Paths', () => {
	
	it(`exports an object`, () => {
		expect(deps).to.be.an('object');
	});
	
	it(`exports "bin" string`, () => {
		expect(deps.bin).to.be.a('string');
	});
	
	it(`exports "include" string`, () => {
		expect(deps.include).to.be.a('string');
	});
	
	it(`has installed the "bin" directory`, () => {
		expect(require('fs').existsSync(deps.bin)).to.be.true;
	});
	
});
